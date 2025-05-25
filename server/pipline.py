from langgraph.graph import StateGraph, END
from nodes.audio_input import capture_audio
from nodes.whisper_transcribe import transcribe_audio
from nodes.memory_update import update_memory
from nodes.resume_query import query_resume
from nodes.graph_query import query_graph
from nodes.llm_response import generate_response
from nodes.tts_output import speak_response

# Define schema with nodes and edges reflecting your flow
schema = {
    "nodes": [
        {"id": "capture", "function": capture_audio},
        {"id": "transcribe", "function": transcribe_audio},
        {"id": "memory", "function": update_memory},
        {"id": "resume", "function": query_resume},
        {"id": "graph", "function": query_graph},
        {"id": "llm", "function": generate_response},
        {"id": "speak", "function": speak_response},
    ],
    "edges": [
        {"from": "capture", "to": "transcribe"},
        {"from": "transcribe", "to": "memory"},
        {"from": "memory", "to": "resume"},
        {"from": "resume", "to": "graph"},
        {"from": "graph", "to": "llm"},
        {"from": "llm", "to": "speak"},
        {"from": "speak", "to": "capture"},
    ],
    "entry_point": "capture"
}

# Create and compile the graph
graph = StateGraph(schema)
interview_graph = graph.compile()

# Run the graph
if __name__ == "__main__":
    print("Starting the interview graph run...")
    result = interview_graph.execute()  # or start(), or process(), etc.
    print(result)

    print("Interview graph finished. Result:")
