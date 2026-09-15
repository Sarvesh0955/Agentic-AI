from ollama import chat

response = chat(
    model="llama3.2",
    # model = "qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Hello"
        }
    ]
)

print(response.message.content)