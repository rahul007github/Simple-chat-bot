import nltk
from nltk.chat.util import Chat, reflections
import random

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi ', 'Heyyy']),

    (r'how are you|how', ['I am good, thank you!', 'I am doing well. How about you?']),

    (r'what is your name|who are you', ['I am a chatbot. You can call me bot!']),

    (r'what is the meaning of life', ['The meaning of life is a mystery. What do you think it is?']),
    (r'who is your developer', ['I was developed by Rahul.']),

    (r'love', ['Love is a wonderful part of life']),

    (r'quit', ['Goodbye','Have a Nice Day!']),
]

unmatched_responses = [
    "I'm not sure I understand. Can you ask me something else?",
    "That's an interesting topic. Let's talk about something else!",
    "I didn't quite catch that. Feel free to ask me another question.",
]

chatbot = Chat(patterns, reflections)

def chat_with_bot():
    print("Hello! I'm bot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("bot: Goodbye!")
            break

        response = chatbot.respond(user_input)

        if response is None:
            print("bot:", random.choice(unmatched_responses))
        else:
            print("bot:", response)

nltk.download('punkt')

chat_with_bot()