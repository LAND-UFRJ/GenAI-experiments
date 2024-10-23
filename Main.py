import openai
import re
import genieacs
import Levenshtein

##############################
#Funcoes não utilizadas na IA#
##############################

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

def processing_dict_no_function(x):
    x = x.split('>>>')[1].strip()
    name = x.split('(')[0]
    args = x.split('(')[1].split(')')[0]
    args = convert_keys_to_string(args)
    args = eval(args)
    return name, args

def find_most_similar_string(target, string_list):
    # Initialize variables to store the best match, its score, and index
    best_match = None
    best_score = float('inf')  # Lower score means more similar
    best_index = -1
    
    # Iterate through each string in the list and compare it with the target
    for index, s in enumerate(string_list):
        score = Levenshtein.distance(target, s)  # Levenshtein distance
        if score < best_score:
            best_score = score
            best_match = s
            best_index = index
    
    return best_match, best_score, best_index

######################################
#fim das funcoes não utilizadas na IA#
######################################


client = openai.OpenAI(
    api_key=  
    base_url= 
)

############################
#Funcoes utilizadas na IA  #
############################

def change(parameter:str, value:str):
    device_id = ''
    acs = genieacs.Connection()
    print(f"Changing parameter {parameter} to {value}")
    acs.task_set_parameter_values(device_id, [[parameter, value]])
    return f"Parameter {parameter} changed to {value}"

def list_devices(device_id:str)->list:
    acs = genieacs.Connection()
    num_dev = acs.device_get_parameter(device_id, "Device.Hosts.HostNumberOfEntries")
    lista = []
    for n in range(1, int(num_dev)+1):
        lista.append(acs.device_get_parameter(device_id, f"Device.Hosts.Host.{n}.HostName"))
    return lista

def info_peer(device_name:str, device_id:str)->list:
    acs = genieacs.Connection()
    num_dev = acs.device_get_parameter(device_id, "Device.Hosts.HostNumberOfEntries")
    lista = []
    for n in range(1, int(num_dev)+1):
        lista.append(acs.device_get_parameter(device_id, f"Device.Hosts.Host.{n}.HostName"))
    best_match, score, index = find_most_similar_string(device_name, lista)


##################################
#Fim das funcoes utilizadas na IA#
##################################

#################
#iteracao com IA#
#################

def adapt_prompt():
    #prompt = input("Enter your prompt: ")
    prompt = 'Can you list the divices connected to the network?'
    text = """This document provides the explanation of genieacs syntax and its translation to natural language. This document is meant to help the model translate a prompt made in natural language into a prompt that has the correct syntax to be used in function calling. Sumerazeing, this model should receive a prompt in natural language and rewrite it in the correct syntax.

    "Device.WiFi.AccessPoint.1.Security.KeyPassphrase":
    This parameter is the network’s password. ‘1’ in the command means that this command will affect the first network. ‘KeyPassphrase’ means that the parameter of that network is the password. The following sentences are examples of natural language prompts and how they translate to the correct syntax:
    ‘Change the password of a network to ‘xyz’.’ becomes: ‘Change Device.WiFi.AccessPoint.1.Security.KeyPassphrase to ‘xyz’.’
    ‘Change the password of the network 2 to ‘xyz’.’ becomes: ’Change Device.WiFi.AccessPoint.2.Security.KeyPassphrase to ‘xyz’.’	
    ‘Change the password of the network N to ‘xyz’ becomes: ’Change Device.WiFi.AccessPoint.N.Security.KeyPassphrase to ‘xyz’’. where N goes from 1 to 14

    "Device.WiFi.SSID.1.SSID":
    This parameter means the name of the SSID 1, that ‘1’ represents which SSID is used. SSID is the name of a network. Usually the SSID 1 means the 2.4GHz network and SSID 3 means the 5GHz network in a router. Usually a router have 14 SSIDs The following sentences are examples of natural language prompts and how they translate to the correct syntax:
    ‘Change the name of a 2.4GHz network to “abcd1234”.’ becomes: ‘Change "Device.WiFi.SSID.1.SSID." to “abcd1234”.’
    ‘Change the name of a 5GHz network to “abcd1234”.’ becomes: ‘ Change "Device.WiFi.SSID.3.SSID." to “abcd1234”.’

    If the user asks to list the devices connected to the network, or the devices connected, you must return the same prompt the user sent you. Foe example:
    'Can you list the devices connected to the network?' should return 'Can you list the devices connected to the network?'
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
        },
        {
            "type": "function",
            "function": {
                "name": "list_devices",
                "description": "List all devices in the ACS",
                "parameters": {},
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
    if tool_calls:
        available_functions = {"change": change,'list_devices': list_devices}  
        messages.append(response_message) 

    for tool_call in tool_calls:
        #caso 1 '>>>functions.add({a: 2, b: 3})'
            if '}' in tool_call.function.name and '>>>functions' in tool_call.function.name:
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

            elif '}' not in tool_call.function.name and '>>>functions' in tool_call.function.name:
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
                temperature=0,) 
                return second_response.choices[0].message.content 
            
            elif '>>>functions' not in tool_call.function.name:
            #caso 3 '>>>divide({ a: 68, b: 58 })'
                name, args = processing_dict_no_function(tool_call.function.name)
                function_to_call = available_functions[name]
                function_response = function_to_call(**args)
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "function",
                        "name": name,
                        "content": f"generate and answer based on the output of the funtion being: {function_response}",
                    }
                )
                second_response = client.chat.completions.create(
                model="Llama-3.2-3B-Instruct-Q8_0",
                messages=messages,
                temperature=0,) 
                return second_response.choices[0].message.content

########################
#fim da iteracao com IA#
########################

def main():
    prompt = adapt_prompt()
    print(tool(prompt))

main()
