#load the environment variables
from dotenv import load_dotenv

load_dotenv()

#Create an API Client to interact with the Anthropic API
from anthropic import Anthropic
client = Anthropic()
model = "claude-haiku-4-5"

#helper functions to add messages to the conversation
def add_user_message(messages, text):
    user_message = {"role": "user","content": text}
    messages.append(user_message)
 
def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant","content": text}
    messages.append(assistant_message)

#make a request to the API
def chat(messages, system=None, temperature=1.0, stop_sequences=None):
    #Build the API call parameters
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    #Only add system parameter if provided
    if system:
        params["system"] = system
    #Only add stop_sequences if provided
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    
    message = client.messages.create(**params)
    return message.content[0].text

#Only run this code when Int.py is executed directly, not when imported
if __name__ == "__main__":
    #Make a starting list of messages
    messages = []

    #Add in the initial user question of "define quantum computing"
    add_user_message(messages, "Define quantum computing in one sentence.")

    #Pass in the list of messages to the chat function to get the response
    answer = chat(messages)

    #Add the assistant's response to the messages list
    add_assistant_message(messages, answer)
    print(messages) #print the messages list to see the conversation

    #add a new user message
    add_user_message(messages, "Write another sentence about quantum computing.")

    #call the chat function again to get the response
    answer = chat(messages)
    print(messages) #print the messages list to see the conversation
    print(answer) #print the answer
