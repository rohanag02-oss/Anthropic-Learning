#Import functions and variables from Int.py
import sys
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

messages = []

prompt = "Generate three different sample AWS CLI Commands. Each should be very short"
add_user_message(messages, prompt)
add_assistant_message(messages, "```")

text = chat(messages, stop_sequences=["```"])
text = text.strip()
print(text)
#add_assistant_message(messages, "```json")
#answer = chat(messages, stop_sequences=["```"])

#print(answer)