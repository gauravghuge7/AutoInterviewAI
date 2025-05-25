from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "test"))

def query_graph_data(query):
    cypher = "MATCH (n) RETURN n LIMIT 3"
    with driver.session() as session:
        result = session.run(cypher)
        return [record["n"] for record in result]
