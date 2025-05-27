def update_memory(state):
    transcript = state["transcript"]
    context = f"Memory updated with: {transcript}"
    return {"context": context, "transcript": transcript}