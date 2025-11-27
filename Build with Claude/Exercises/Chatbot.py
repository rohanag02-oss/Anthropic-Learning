#Import functions and variables from Int.py
import sys
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

#Make an initial list of messages
messages = []

#Use a 'while true' loop to keep the chatbot running
while True:
    #Get user input
    user_input = input("> ")
    print(">", user_input)
    if user_input.lower() in ["quit", "exit", "bye"]:
        break
    #Add the user input to the messages list
    add_user_message(messages, user_input)
    #Call the chat function to get the response
    answer = chat(messages)
    #Add the assistant's response to the messages list
    add_assistant_message(messages, answer)
    #Print the messages list to see the conversation
    print("---")
    print(answer)
    print("---")