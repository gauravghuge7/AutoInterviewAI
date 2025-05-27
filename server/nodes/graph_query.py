from utils.neo4j_utils import query_graph_data

def query_graph(state):
    graph_data = query_graph_data(state["transcript"])
    return {"graph_data": graph_data, **state}