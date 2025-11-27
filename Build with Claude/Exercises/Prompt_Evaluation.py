#Import functions and variables from Int.py
import sys
import json
from pathlib import Path
# Add parent directory to path to import Int.py
sys.path.insert(0, str(Path(__file__).parent.parent))
from Int import add_user_message, add_assistant_message, chat, client, model

def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
  {
    "task": "Description of task",
  },
  ...additional
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""
    messages =[]
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)

def run_prompt(test_case):
    """Merge the prompt and test case input, then returns thre result"""
    prompt = f"""
please solve the following task:

{test_case["task"]}
"""
    messages =[]
    add_user_message(messages, prompt)
    output = chat(messages)
    return output

def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)

    #TODO - Grading
    score = 10

    return{
        "output": output,
        "test_case": test_case,
        "score": score

    }

def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []

    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    return results

#Only run this code when Prompt Evaluation.py is executed directly, not when imported
if __name__ == "__main__":
    # Generate dataset (uncomment to regenerate)
    # dataset = generate_dataset()
    # print(json.dumps(dataset, indent=2))
    # with open("dataset.json", "w") as f:
    #     json.dump(dataset, f, indent=2)
    
    # Run evaluation on existing dataset
    with open("dataset.json", "r") as f:
        dataset = json.load(f)
    
    results = run_eval(dataset)
    print(json.dumps(results, indent=2))