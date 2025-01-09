from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from neo4j import GraphDatabase


llm = ChatOpenAI()

uri = ""
username = ""
password = ""

driver = GraphDatabase.driver(uri, auth=(username, password))

def get_all():
    with driver.session() as session:
        query = '''
        MATCH (n)
        RETURN n
        '''
        result = session.run(query)
        lista = []
        for record in result:
            lista.append(record)
        session.close()
    return lista

def get_N(node:str, degrees:int)->list:
    
    with driver.session() as session:
        query = '''
        MATCH (startNode {id: "%s"})-[r*1..%s]-(connectedNode)
        RETURN connectedNode, r
        ''' % (node,degrees)
        result = session.run(query)
        unique_nodes = set()  # Use a set to store unique node IDs
        lista = []
        for record in result:
            # Extract the node ID from the record
            node_id = record["connectedNode"].get("id")
            if node_id not in unique_nodes:
                unique_nodes.add(node_id)
                # Extract the relationships
                relationships = []
                for rel in record["r"]:
                    relationships.append({
                        "type": rel.type,
                        "start_node_id": rel.start_node.get("id"),
                        "end_node_id": rel.end_node.get("id")
                    })
                # Clean up the record to extract the node information
                node_info = {
                    "node_id": node_id,
                    "labels": list(record["connectedNode"].labels),
                    "properties": dict(record["connectedNode"]),
                    "relationships": relationships
                }
                lista.append(node_info)
        session.close()
    return lista

def get_all_node_names():
    with driver.session() as session:
        query = '''
        MATCH (n)
        RETURN n.id AS node_name
        '''
        result = session.run(query)
        node_names = [record["node_name"] for record in result]
        session.close()
    return node_names

def get_all_relationships():
    with driver.session() as session:
        query = '''
        MATCH (startNode)-[r]->(endNode)
        RETURN startNode.id AS start_node_id, 
               type(r) AS relationship_type, 
               endNode.id AS end_node_id
        '''
        result = session.run(query)
        relationships = []
        for record in result:
            relationships.append(record["relationship_type"])
        relationships = set(relationships)
        session.close()
    return relationships

def main(query):
    tools = [get_N]
    tool_messages = [SystemMessage(f'You are an AI assistant the is being used to query a graph database. Keep in mind that the nodes that exist in that DB are: {get_all_node_names()} and the relations among them are of the following types: {get_all_relationships()}',)
                , HumanMessage(query)]
    llm_tools = llm.bind_tools(tools)
    response = llm_tools.invoke(query)
    package = response.content.split(';')

    graph_query = []
    for x in package:
        x= eval(x)
        print(x)
        name , param = x['name'], x['parameters']
        result = eval(name)(**param)
        graph_query.append(result)


    messages = [SystemMessage(f'You are an AI assistant that will answer questions about this data: {graph_query}'), HumanMessage(query)]
    answer = llm.invoke(messages).content
    return answer
