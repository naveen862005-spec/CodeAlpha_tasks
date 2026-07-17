# Basic Chatbot

def chatbot():
    print("===== BASIC CHATBOT =====")
    print("Type 'bye' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Simple Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

# Run the chatbot
chatbot()