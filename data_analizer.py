# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import psycopg2  # For PostgreSQL database connection
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's language model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage  # For message handling in the LLM
import chromadb  # For vector storage and retrieval
from langchain_openai import OpenAIEmbeddings  # For generating text embeddings

# Connection parameters for the PostgreSQL database
conn_params = {
    "host": "",  # Database server IP address
    "port": ,  # Default PostgreSQL port
    "database": "",  # Name of the database
    "user": "",  # Database username
    "password": ""  # Database password
}

# Function to establish a connection to the PostgreSQL database
def get_db_connection():
    try:
        conn = psycopg2.connect(**conn_params)  # Attempt to connect to the database
        return conn  # Return the connection object if successful
    except Exception as e:
        return None  # Return None if connection fails

# Initialize the language model (LLM) with custom base URL and API key
llm = ChatOpenAI(base_url='', api_key='')

# Function to get the maximum value of a specific parameter from the WiFi stats table
def get_max(param):
    conn = get_db_connection()  # Get database connection
    if conn is None:
        return None  # Return None if connection fails
    
    # SQL query to fetch relevant columns from the WiFi stats table
    query = """
    SELECT time, mac_address, hostname, signal_strength, packets_sent, packets_received
    FROM wifi_stats """
    
    with conn.cursor() as cursor:
        cursor.execute(query)  # Execute the query
        results = cursor.fetchall()  # Fetch all results
        columns = ["time", "mac_address", "hostname", "signal_strength", "packets_sent", "packets_received"]
        df = pd.DataFrame(results, columns=columns)  # Convert results to a DataFrame
    conn.close()  # Close the database connection
    return df[param].max()  # Return the maximum value of the specified parameter

# Function to get the minimum value of a specific parameter from the WiFi stats table
def get_min(param):
    conn = get_db_connection()  # Get database connection
    if conn is None:
        return None  # Return None if connection fails
    
    # SQL query to fetch relevant columns from the WiFi stats table
    query = """
    SELECT time, mac_address, hostname, signal_strength, packets_sent, packets_received
    FROM wifi_stats """
    
    with conn.cursor() as cursor:
        cursor.execute(query)  # Execute the query
        results = cursor.fetchall()  # Fetch all results
        columns = ["time", "mac_address", "hostname", "signal_strength", "packets_sent", "packets_received"]
        df = pd.DataFrame(results, columns=columns)  # Convert results to a DataFrame
    conn.close()  # Close the database connection
    return df[param].min()  # Return the minimum value of the specified parameter

# Function to get the average value of a specific parameter from the WiFi stats table
def get_avg(param):
    conn = get_db_connection()  # Get database connection
    if conn is None:
        return None  # Return None if connection fails
    
    # SQL query to fetch relevant columns from the WiFi stats table
    query = """
    SELECT time, mac_address, hostname, signal_strength, packets_sent, packets_received
    FROM wifi_stats """
    
    with conn.cursor() as cursor:
        cursor.execute(query)  # Execute the query
        results = cursor.fetchall()  # Fetch all results
        columns = ["time", "mac_address", "hostname", "signal_strength", "packets_sent", "packets_received"]
        df = pd.DataFrame(results, columns=columns)  # Convert results to a DataFrame
    conn.close()  # Close the database connection
    return df[param].mean()  # Return the average value of the specified parameter

# Function to count the number of unique values for a specific parameter in the WiFi stats table
def count(param):
    conn = get_db_connection()  # Get database connection
    if conn is None:
        return None  # Return None if connection fails
    
    # SQL query to fetch relevant columns from the WiFi stats table
    query = """
    SELECT time, mac_address, hostname, signal_strength, packets_sent, packets_received
    FROM wifi_stats """
    
    with conn.cursor() as cursor:
        cursor.execute(query)  # Execute the query
        results = cursor.fetchall()  # Fetch all results
        columns = ["time", "mac_address", "hostname", "signal_strength", "packets_sent", "packets_received"]
        df = pd.DataFrame(results, columns=columns)  # Convert results to a DataFrame
    conn.close()  # Close the database connection
    unique_values = df[param].unique()  # Get unique values for the specified parameter
    return len(unique_values)  # Return the count of unique values

# Function to enumerate unique values for a specific parameter in the WiFi stats table
def enum(param):
    conn = get_db_connection()  # Get database connection
    if conn is None:
        return None  # Return None if connection fails
    
    # SQL query to fetch relevant columns from the WiFi stats table
    query = """
    SELECT time, mac_address, hostname, signal_strength, packets_sent, packets_received
    FROM wifi_stats """
    
    with conn.cursor() as cursor:
        cursor.execute(query)  # Execute the query
        results = cursor.fetchall()  # Fetch all results
        columns = ["time", "mac_address", "hostname", "signal_strength", "packets_sent", "packets_received"]
        df = pd.DataFrame(results, columns=columns)  # Convert results to a DataFrame
    conn.close()  # Close the database connection
    unique_values = df[param].unique()  # Get unique values for the specified parameter
    return unique_values  # Return the unique values

# Initialize ChromaDB client for vector storage and retrieval
client = chromadb.HttpClient(host='', port=)
colection = client.get_or_create_collection(name='teste', embedding_function=None)

# Initialize OpenAI embeddings for text embedding
openai_embeddings = OpenAIEmbeddings(base_url='', api_key='')

# Function to generate embeddings for a given text using OpenAI embeddings
def get_embedding(text):
    return openai_embeddings.embed_query(text)

# Example usage of the functions and LLM to answer a query
tools = [get_avg, get_max, get_min, count, enum]  # List of available tools/functions

query = "What was the highest amount of packets sent? And the lowest?"  # User query

# Query ChromaDB for relevant documents based on the query embedding
RAG_result = colection.query(query_embeddings=get_embedding(query), n_results=3, include=['documents'])

# Construct the prompt for the LLM with the query and context from ChromaDB
prompt = f''' 
<<<Query>>> 
{query}
<<<Query>>>

<<<Context>>>
{RAG_result['documents'][0]}
<<<Context>>>
'''

# Prepare messages for the LLM
messages = [HumanMessage(prompt)]
llm_tool = llm.bind_tools(tools)  # Bind the available tools to the LLM
response = llm_tool.invoke(messages)  # Invoke the LLM with the prepared messages
package = response.content.split(';')  # Split the response content

# Process the LLM response and generate the final answer
for x in package:
    x = eval(x)  # Evaluate the response to get the function name and parameters
    name, param = x['name'], x['parameters']
    result = eval(name)(**param)  # Execute the function with the provided parameters
    messages.append(SystemMessage(f'You are an AI assistant. I will give you the result from a function and you have to write an answer based only on it. The format of the datetime is YYYY-MM-DD HH:MM:SS, given that today is {today}.'))
    messages.append(AIMessage(str(x)))  # Append the function call to the messages
    messages.append(SystemMessage(str(result)))  # Append the function result to the messages
answer = llm.invoke(messages)  # Generate the final answer using the LLM
print(answer.content)  # Print the final answer
