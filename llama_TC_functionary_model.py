import openai
import json
import pandas as pd

client = openai.OpenAI(
    api_key= '',
    base_url= ''
)

def maxi_tool(column: str) -> float:
    df = pd.read_csv('dados.csv')
    #print(f"Column received: {column}")
    return df[column].max()

def mini_tool(column: str) -> float:
    df = pd.read_csv('dados.csv')
    #print(f"Column received: {column}")
    return df[column].min()

def mean_tool(column: str) -> float:
    df = pd.read_csv('dados.csv')
    #print(f"Column received: {column}")
    return df[column].mean()

def std_tool(column: str) -> float:
    df = pd.read_csv('dados.csv')
    #print(f"Column received: {column}")
    return df[column].std()

def run_conversation():
    # Step 1: send the conversation and available functions to the model
    messages = [
        {
            "role": "user",
            "content": "What's the lowest value in the bitreate column? ",
        }
    ]
    tools = [
    {
        "type": "function",
        "function": {
            "name": "maxi_tool",
            "description": "Get the maximum value of a column in the dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "column": {
                        "type": "string",
                        "description": "The name of the column to get the maximum value of",
                    }
                },
                "required": ["column"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mini_tool",
            "description": "Get the minimum value of a column in the dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "column": {
                        "type": "string",
                        "description": "The name of the column to get the minimum value of",
                    }
                },
                "required": ["column"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mean_tool",
            "description": "Get the mean value of a column in the dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "column": {
                        "type": "string",
                        "description": "The name of the column to get the mean value of",
                    }
                },
                "required": ["column"],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "std_tool",
            "description": "Get the standard deviation of a column in the dataset",
            "parameters": {
                "type": "object",
                "properties": {
                    "column": {
                        "type": "string",
                        "description": "The name of the column to get the standard deviation of",
                    }
                },
                "required": ["column"],
            },
        }
    }
]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        temperature=1,
        #tool_choice='required'
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "maxi_tool": maxi_tool,
            "mini_tool": mini_tool,
            "mean_tool": mean_tool,
            "std_tool": std_tool,
        }  
        messages.append(response_message)  # extend conversation with assistant's reply
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name.split('\n')[0].split('.')[-1]
            function_args = json.loads(tool_call.function.name.split('\n')[1])
            function_to_call = available_functions[function_name]
            function_response = function_to_call(
                column=function_args.get("column"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": str(function_response),
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response.choices[0].message.content


print(run_conversation())
