import openai

def generate_response(state):
    prompt = f"Resume Info: {state['resume_data']}\nGraph: {state['graph_data']}\nUser said: {state['transcript']}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Interview assistant."},
                  {"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message["content"]
    return {"response": answer, **state}