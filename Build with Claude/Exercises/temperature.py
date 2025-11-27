#Import functions and variables from Int.py
import sys
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

messages = []
add_user_message(
    messages,
    "Generate a one sentence review of the show selling sunset on Netfilx", 
)

answer = chat(messages, temperature=0.0)

print(answer)