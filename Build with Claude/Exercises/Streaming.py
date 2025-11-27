#Import functions and variables from Int.py
import sys
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

messages = []

add_user_message(messages, "write a 1 sentence description of a fake database")

with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
    
    # Get the final message after streaming is complete
    # Must be called while stream is still in scope
    final_message = stream.get_final_message()
    print("\n\nFinal message:", final_message)

    