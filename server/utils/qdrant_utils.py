# utils/qdrant_utils.py
import requests
import json
import uuid

QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "resumes"

def init_qdrant_collection():
    requests.put(f"{QDRANT_URL}/collections/{COLLECTION_NAME}", json={
        "vectors": {"size": 1536, "distance": "Cosine"}
    })

def upload_resume_to_qdrant(text, metadata):
    from utils.resume_processing import embed_text
    vector = embed_text(text)
    payload = {
        "points": [{
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": metadata
        }]
    }
    requests.put(f"{QDRANT_URL}/collections/{COLLECTION_NAME}/points", json=payload)

def query_qdrant(query_text):
    from utils.resume_processing import embed_text
    vector = embed_text(query_text)
    payload = {"vector": vector, "top": 3}
    response = requests.post(f"{QDRANT_URL}/collections/{COLLECTION_NAME}/points/search", json=payload)
    if response.status_code == 200:
        return response.json().get("result", [])
    return []
