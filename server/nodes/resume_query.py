from utils.qdrant_utils import query_qdrant

def query_resume(state):
    resume_chunks = query_qdrant(state["transcript"])
    return {"resume_data": resume_chunks, **state}
