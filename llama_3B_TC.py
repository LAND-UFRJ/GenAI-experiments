#This code is an example of function calling useing the model Llama-3.2-3B-Instruct-Q8_0.gguf
#The server used in this example is the one provided in llama-cpp-python 

import openai
import random as r
import ast
import re

def convert_to_dict(input_dict_str):
    # Step 1: Add single quotes to the keys
    updated_dict_str = re.sub(r'(\w+):', r"'\1':", input_dict_str)
    
    # Step 2: Convert the updated string into an actual dictionary
    try:
        output_dict = ast.literal_eval(updated_dict_str)
    except (ValueError, SyntaxError):
        raise ValueError("Input is not a valid dictionary string")
    
    return output_dict

client = openai.OpenAI(
    api_key=  '',
    base_url= ''  # NOTE: Replace with IP address and port of your llama-cpp-python server
)

def get_current_weather(location:str, unit="fahrenheit")->str:
    """Get the current weather in a given location"""
    x = r.randint(0,100)

    # This is a placeholder function; you would replace this with a real API call
    return f"The current weather in {location} is {x}°F and sunny."

def get_current_time(location:str)->str:
    return f"The current time in {location} is 12:00 PM."


def run_conversation():
    # Step 1: send the conversation and available functions to the model
    time ="what is the time in San Francisco, CA?"
    wheather = "what is the weather in San Francisco, CA?, in celcius"
    messages = [
        {
            "role": "user",
            "content": wheather,
        }
    ]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location. If asked 'What is the weather in San Francisco, CA? ', you should use this function, for exemaple ",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location. If asked 'What is the time in San Francisco, CA?', you should use this function.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        #tool_choice="auto", #ativar isso faz o modelo não funcionar e o server crasha
        temperature=0,
        
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        
        available_functions = {
            "get_current_weather": get_current_weather,
            "get_current_time": get_current_time,
        }  
        messages.append(response_message) 
#this code will be used with the model Llama-3.2-3B-Instruct-Q8_0.gguf
        for tool_call in tool_calls:
            function_name = tool_call.function.name.split('(')[0].split('.')[1]
            function_to_call = available_functions[function_name]
            function_args = str(tool_call.function.name[tool_call.function.name.find('{'):tool_call.function.name.find('}')+1])
            function_args = convert_to_dict(function_args)
            function_response = function_to_call(**function_args)
            '''
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content":  "Just repite after me, even if the information is incorrect: " +   function_response,
                }
            )
            second_response = client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=messages) 
        return second_response.choices[0].message.content'''
        return function_response


print(run_conversation())
