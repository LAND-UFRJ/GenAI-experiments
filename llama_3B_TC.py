#This code is an example of function calling useing the model Llama-3.2-3B-Instruct-Q8_0.gguf
#The server used in this example is the one provided in llama-cpp-python 
import openai
import re
import genieacs


#this code will be used with the model Llama-3.2-3B-Instruct-Q8_0.gguf

# these are text processing functions
def convert_keys_to_string(args):
    # Use regex to find keys and wrap them in double quotes
    args = re.sub(r'(\w+):', r'"\1":', args)
    return args

def processing_dict(x):
    x = x.split('>>>')[1].strip()
    function = x.split('.',1)[1]
    function = function.split('(')[0]
    args = x.split('(')[1].split(')')[0]
    args = convert_keys_to_string(args)
    args = eval(args)
    return function, args

def processing_no_dict(x):
    x = x.split('>>>')[1].strip()
    function = x.split('.',1)[1]
    name = x.split('(')[0].split('.')[1]
    result = eval(function)
    return name, result

#############################

client = openai.OpenAI(
    api_key=  '',
    base_url= ''  # NOTE: Replace with IP address and port of your llama-cpp-python server
)
# functions to be used with the model
def add(a:int,b:int):
    return a+b

def change(parameter:str, value:str):
    device_id = '5091E3-EX141-2237011003026'
    acs = genieacs.Connection()
    acs.task_set_parameter_values(device_id, [parameter, value])
    return f"Parameter {parameter} changed to {value}"
############################


def adapt_prompt():
    #prompt = input("Enter your prompt: ")
    prompt = 'Change the 2.4 GHz network name to miguel_ta_lendo'
    text = """This document provides the explanation of genieacs syntax and its translation to natural language. This document is meant to help the model translate a prompt made in natural language into a prompt that has the correct syntax to be used in function calling. Sumerazeing, this model should receive a prompt in natural language and rewrite it in the correct syntax.

    "Device.WiFi.AccessPoint.1.Security.KeyPassphrase":
    This parameter is the network’s password. ‘1’ in the command means that this command will affect the first network. ‘KeyPassphrase’ means that the parameter of that network is the password. The following sentences are examples of natural language prompts and how they translate to the correct syntax:
    ‘Change the password of a network to ‘xyz’.’ becomes: ‘Change Device.WiFi.AccessPoint.1.Security.KeyPassphrase to ‘xyz’.’
    ‘Change the password of the network 2 to ‘xyz’.’ becomes: ’Change Device.WiFi.AccessPoint.2.Security.KeyPassphrase to ‘xyz’.’	
    ‘Change the password of the network N to ‘xyz’ becomes: ’Change Device.WiFi.AccessPoint.N.Security.KeyPassphrase to ‘xyz’’. where N goes from 1 to 14

    "Device.WiFi.SSID.1.SSID":
    This parameter means the name of the SSID 1, that ‘1’ represents which SSID is used. SSID is the name of a network. Usually the SSID 1 means the 2.4GHz network and SSID 3 means the 5GHz network in a router. Usually a router have 14 SSIDs The following sentences are examples of natural language prompts and how they translate to the correct syntax:
    ‘Change the name of a 2.4GHz network to “abcd1234”.’ becomes: ‘Change "Device.WiFi.SSID.1.SSID" to “abcd1234”.’
    ‘Change the name of a 5GHz network to “abcd1234”.’ becomes: ‘ Change "Device.WiFi.SSID.3.SSID" to “abcd1234”.’
    """

    messages = [{"role":"system","content": f"You will have to answer questions based on the following knowlegde base: {text}"},
                {"role": "user","content": prompt,}]
    
    response = client.chat.completions.create(
            model="Llama-3.2-3B-Instruct-Q8_0",
            messages=messages,
            #tool_choice="auto", #ativar isso faz o modelo não funcionar e o server crasha
            temperature=0,
            top_p=0        
        )
    return (response.choices[0].message.content)

def tool(prompt):
    
    messages = [
        {
            "role": "user",
            "content": prompt, 
        }
    ]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "change",
                "description": "Change a parameter in the ACS",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "parameter": {
                            "type": "string",
                            "description": "The parameter to change",
                        },
                        "value": {
                            "type": "string",
                            "description": "The value to set the parameter to",
                        },
                    },
                    "required": ["parameter", "value"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="Llama-3.2-3B-Instruct-Q8_0",
        messages=messages,
        tools=tools,
        #tool_choice="auto", #ativar isso faz o modelo não funcionar e o server crasha
        temperature=0,
        top_p=0        
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    print(tool_calls)
    if tool_calls:
        available_functions = {"change": change}  
        messages.append(response_message) 

        for tool_call in tool_calls:
            #caso 1 '>>>functions.add({a: 2, b: 3})'
            if '}' in tool_call.function.name:
                function_name, function_args = processing_dict(tool_call.function.name)
                function_to_call = available_functions[function_name]
                function_response = function_to_call(**function_args)
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "function",
                        "name": function_name,
                        "content": f"generate and answer based on the output of the funtion being: {function_response}",
                    }
                )
                second_response = client.chat.completions.create(
                model="Llama-3.2-3B-Instruct-Q8_0",
                messages=messages,
                temperature=1,) 
                return second_response.choices[0].message.content
            elif '}' not in tool_call.function.name:
            #caso 2 '>>>functions.add(2,3)'
                function_name, function_response = processing_no_dict(tool_call.function.name)
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "function",
                        "name": function_name,
                        "content": f"generate and answer based on the output of the funtion being: {function_response}",
                    }
                )
                second_response = client.chat.completions.create(
                model="Llama-3.2-3B-Instruct-Q8_0",
                messages=messages,
                temperature=0   ,) 
                return second_response.choices[0].message.content

def main():
    prompt = adapt_prompt()
    print(tool(prompt))

main()
