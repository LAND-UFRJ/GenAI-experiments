import openai
import json
import numpy as np
import pandas as pd

client = openai.OpenAI(
    api_key=  # can be a senha de sempre
    base_url= #olhar na planilha,  # NOTE: Replace with IP address and port of your llama-cpp-python server
)

random_array = np.random.rand(10, 2)  
df = pd.DataFrame(random_array, columns=["A", "B"])
df.to_csv("random_data.csv", index=False)


def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    # This is a placeholder function; you would replace this with a real API call
    return f"The current weather in {location} is 72°F and sunny."


def run_conversation():
    # Step 1: send the conversation and available functions to the model
    messages = [
        {
            "role": "user",
            "content": "What's the weather like in  Rio dejaneiro? And what is the weather in San Francisco, CA?",
        }
    ]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
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
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
        temperature=0
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name.split('\n')[0].split('.')[-1]
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response.choices[0].message.content


print(run_conversation())