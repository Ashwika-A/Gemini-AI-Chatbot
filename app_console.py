from chatbot import get_response

print("Gemini AI Chatbot (type 'exit' to quit)")

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    response = get_response(prompt)
    print(f"Bot: {response}")