# CodeAlpha Task 4 - Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you."

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can respond to simple predefined messages."

    elif user_input == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


print("================================")
print("       BASIC CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower().strip() == "bye":
        break

print("\nChatbot session ended.")