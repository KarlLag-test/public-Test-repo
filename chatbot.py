import sys

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "I'm a simple chatbot. You can greet me or say 'bye' to exit."
    else:
        return "I'm not sure how to respond to that."

def main():
    print("Welcome to the Rule-Based Chatbot! Type 'bye' or 'exit' to quit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

if __name__ == "__main__":
    main()