print(" Hello! I'm Bharath ChatBot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello there! How can I help you today?")
    elif user_input == "how are you":
        print("Bot: I'm just code, but I'm running fine! ")
    elif user_input == "what is your name":
        print("Bot: I'm your friendly Bharath chatbot.")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a great day! ")
        break
    elif "weather" in user_input:
        print("Bot: I'm not connected to the internet, but I hope it's sunny!")
    elif "help" in user_input:
        print("Bot: You can ask me simple questions like 'hi', 'how are you', 'what is your name', or say 'bye' to exit.")
    else:
        print("Bot: I'm not sure how to respond to that.")
