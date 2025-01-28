import ollama
desiredModel = 'deepseek-r1:1.5b'
questionToAsk = 'What is the capital of India?'

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'user',
        'content': questionToAsk
    }
])

OllamaResponse = response['message']['content']

print(OllamaResponse)

with open("OutputOllama.txt", "w", encoding="utf-8") as text_file:
    text_file.write(OllamaResponse)