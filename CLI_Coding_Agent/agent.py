from openai import OpenAI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv
import json
import requests
import os


load_dotenv()

client = OpenAI()

def run_command(cmd : str):
    result = os.system(cmd)
    return result


available_tools = {
    "run_command" : run_command
}

SYSTEM_PROMPT = """
        You 're an Expert AI Assistant in resolving user queries using chain of thought.
        You work on START, PLAN, OBSERVE and OUTPUT steps.
        You needs to be PLAN first what needs to be done. The PLAN can be multiple steps.
        Once you think enough plan is done, finally you can give the output.
        You can call a tool if required from the available tools.
        For every tool call,, wait for the OBSERVE step with the tool's result.

        Rules:
        - Follow the JSOM format strictly
        - Only one step at a time
        - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times), TOOL (when the tool is called), OBSERVE (obser tools result after the tool call) finally OUTPUT (which is going to the displayed to the user).

        Output JSON Format:
        { "step": "START" | "PLAN" | "OUTPUT" | "TOOL" | "OBSERVE",
             "content": "string",
             "tool": "string",
             "input": "string"
        }

        Available tools :
        - run_command(cmd : str)
"""
print("\n\n")


class MyOutputFormat(BaseModel):
    step : str = Field(..., description= "The ID of the step. Example PLAN, OUTPUT,TOOL, etc.")
    content : str = Field(None, description= "The optiona string content for the step.")
    tool : str = Field(None, description= "The ID of tool to call.")
    input : str = Field(None, description= "The input params for the tool.")

message_history = [
    {
        "role" : "system", "content" : SYSTEM_PROMPT
    }
]

while True:
    user_query = input("Enter the query 👉🏻 ")
    message_history.append({"role" : "assistant", "content" : user_query})

    while True:
        response = client.chat.completions.parse(
            model= "gpt-4o",
            response_format= MyOutputFormat,
            messages=message_history
        )
        raw_result = response.choices[0].message.content
        message_history.append({"role" : "assistant", "content" : raw_result})

        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            print("🔥 ", parsed_result.step)
            continue
        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print(f"🛠️: {tool_to_call}({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"🛠️: {tool_to_call}({tool_input}) = {tool_response}")
            message_history.append(
                {
                    "role" : "developer" , "content" : json.dumps(
                        {
                            "step" : "OBSERVE",
                            "tool" : tool_to_call,
                            "input" : tool_input,
                            "output" : tool_response
                        }
                    )
                }
            )
            continue

        if parsed_result.step == "PLAN":
            print("🧠: ",parsed_result.content)
            continue
        
        if parsed_result.step == "OUTPUT":
            print("🤖", parsed_result.content)
            break
            
