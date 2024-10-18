#This code is an example of function calling useing the model Llama-3.2-3B-Instruct-Q8_0.gguf
#The server used in this example is the one provided in llama-cpp-python 
import openai

def processing(x):
    x = x.split('>>>')[1].strip()
    function = x.split('.')[1]
    name = x.split('(')[0].split('.')[1]
    result = eval(function)
    return name, result

client = openai.OpenAI(
    api_key=  '',
    base_url= ''  # NOTE: Replace with IP address and port of your llama-cpp-python server
)

def add(a:int,b:int):
    return a+b


def run_conversation_ll3BQ8():
    # Step 1: send the conversation and available functions to the model
    prompt = 'What is 3 + 4?'
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
                "name": "add",
                "description": "Add two numbers together",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "integer",
                            "description": "The first number to add",
                        },
                        "b": {
                            "type": "integer", 
                            "description": "The second number to add",
                            },
                    },
                    "required": ["a", "b"],
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
    if tool_calls:
        
        available_functions = {"add": add,}  
        messages.append(response_message) 
#this code will be used with the model Llama-3.2-3B-Instruct-Q8_0.gguf
    
        for tool_call in tool_calls:
            function_name, function_response = processing(tool_call.function.name)
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
            temperature=0,
            top_p=0
            ) 
        return second_response.choices[0].message.content

print(run_conversation_ll3BQ8())
