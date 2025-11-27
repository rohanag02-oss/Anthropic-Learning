#Import functions and variables from Int.py
import sys
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

messages = []
system = "You are a patient math tutor. Do not direct the user to a specific formula or step. Just guide them through the problem step by step."

add_user_message(messages, "how do I solve 5x+3=2 for x?")
answer = chat(messages, system=system)
print(answer)