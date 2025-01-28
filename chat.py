import ollama # type: ignore

desiredModel = 'deepseek-r1:1.5b'

def chat_with_ollama(prompt):
    try:
        response = ollama.chat(model=desiredModel, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    response = chat_with_ollama(user_prompt)
    print("Ollama's response:\n", response)