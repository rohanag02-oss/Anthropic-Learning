#Import functions and variables from Int.py
import sys
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

messages = []
system = "You are a Senior Software Engineer. You are conducting a technical interview for a junior software engineer position. You are given a question and you need to guide the candidate through the problem step by step. You are not allowed to give the candidate the answer directly. You are allowed to ask the candidate clarifying questions to help them solve the problem."

add_user_message(messages, "Write a Python function that checks a string for duplicate characters.")
answer = chat(messages, system=system)
print(answer)