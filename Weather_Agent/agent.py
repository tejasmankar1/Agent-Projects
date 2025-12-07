from dotenv import load_dotenv
from openai import OpenAI
import requests
from pydantic import BaseModel,Field
from typing import Optional
import json

load_dotenv()
client = OpenAI()

def weather_agent(city : str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f" The Weather in {city} is {response.text}"
    return "Something went wrong"


available_tools = {
    "weather_agent" : weather_agent
}

SYSTEM_PROMPT = """
        You 're an expert AI Assistant in resloving user queries usingg chain of thought.
        You work on START, PLAN and OUTPUT steps.
        You need to first PLAN what needs to be done. The PLAN multiple steps.
        Once you think enough PLAN has been done, finally you can give an OUTPUT.
        You can also call a tool if required from the list of availaable tools.
        for every tool call wait for the observe step which is the output from the called tools..

        Rules;
        - Strictly follow the given JSON output format
        - Only run one step at a time.
        - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and 
        finally OUTPUT (which is going to displayed to the user).

        Output JSON format:
        {"step" : "START" | "PLAN" | "OUTPUT" | "TOOL" | "OBSERVE" ,
            "content" : "string",
            "tool" : "string",
            "input" : "string"
        }

        Available Tools:
        - weather_agent(city : str): Takes city name as an input string and returns the weather info about the city.

        Example : 
        START : What is the weather of Delhi?
        PLAN : {"step" : "PLAN" , "content" : "Seems like user is interested in getting weather of Delhi in India"}
        PLAN : {"step" : "PLAN" , "content" : "Let see if we have any available tool from the list of available tools"}
        PLAN : {"step" : "PLAN" , "content" : "Great, we have weather_agent tool available for this query."}
        PLAN : {"step" : "PLAN" , "content" : "I need to call weather_agent tool fro delhi as input for city"}
        PLAN : {"step" : "TOOL" , "tool" : "weather_agent" , "input" : "Delhi"}
        PLAN : {"step":"OBSERVE","content":"The Weather in Delhi is Sunny +25°C","tool":"weather_agent","input":"Delhi"}
        PLAN : {"step" : "PLAN" , "content" : "Great, I got the weather info about Delhi"}
        PLAN : {"step" : "OUTPUT" , "content" : "The Current temperature in Delhi is 20°C with cloudy sky."}
"""

print("\n\n")

class MyOutputFormat(BaseModel):
    step : str = Field(..., description= " The ID of the step. Example PLAN, OUTPUT, TOOL, etc.")
    content : Optional[str] = Field(None, description= "The optional string content for the step.")
    tool : Optional[str] = Field(None,  description= " The ID of the tool to call.")
    input : Optional[str] = Field(None, description= "The input parameters for the tool.")

message_history = [
    {"role" : "system", "content" : SYSTEM_PROMPT}
]

while True:
    user_qery = input("Query 👉🏻 ")
    message_history.append({"role" : "user", "content" : user_qery})

    while True:
        response = client.chat.completions.parse(
            model = "gpt-4o",
            response_format = MyOutputFormat,
            messages = message_history
        )
        raw_result = response.choices[0].message.content
        message_history.append({"role" : "assistant" , "content" : raw_result})

        parsed_reslut  = response.choices[0].message.parsed

        if parsed_reslut.step == "START":
            print("🔥 ", parsed_reslut.content)
            continue
        if parsed_reslut.step == "TOOL":
            tool_to_call = parsed_reslut.tool
            tool_input = parsed_reslut.input
            print(f"🛠️ :  {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"🛠️: {tool_to_call}  ({tool_input}) = {tool_response}")
            message_history.append({
                "role" : "developer", "content" : json.dumps(
                    {
                        "step" : "OBSERVE", "tool": tool_to_call ,"input" : tool_input, "output": tool_response
                    }
                )
            })
            continue

        if parsed_reslut.step == "PLAN" :
            print("🧠: ",  parsed_reslut.content)
            continue
        if parsed_reslut.step == "OUTPUT" :
            print("🤖: ", parsed_reslut.content )
            break
print("\n\n")


