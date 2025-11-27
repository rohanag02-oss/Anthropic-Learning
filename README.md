# Build with Claude

A collection of Python exercises and examples for working with the Anthropic Claude API. This project demonstrates various features including system prompts, temperature control, streaming responses, and prompt evaluation.

## Project Structure

```
.
├── Int.py                    # Main API client and helper functions
├── dataset.json              # Evaluation dataset for prompt testing
└── Exercises/
    ├── Chatbot.py            # Interactive chatbot example
    ├── Controlling Output.py # Output control examples
    ├── Prompt Evaluation.py  # Prompt evaluation framework
    ├── Streaming.py          # Streaming response example
    ├── System Prompts.py     # System prompt examples
    ├── System_prompt_exercise.py
    └── temperature.py        # Temperature parameter examples
```

## Prerequisites

- Python 3.7 or higher
- Anthropic API key

## Setup

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd "Build with Claude"
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```bash
   cp .env.example .env
   ```

4. Add your Anthropic API key to the `.env` file:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

## Usage

### Basic Example

Run the main example:
```bash
python Int.py
```

### Exercises

Each exercise demonstrates different features of the Claude API:

- **Chatbot**: Interactive chatbot with conversation history
  ```bash
  python Exercises/Chatbot.py
  ```

- **Streaming**: Real-time streaming responses
  ```bash
  python Exercises/Streaming.py
  ```

- **Temperature Control**: Examples with different temperature settings
  ```bash
  python Exercises/temperature.py
  ```

- **Prompt Evaluation**: Evaluate prompts against a dataset
  ```bash
  python Exercises/Prompt Evaluation.py
  ```

## Features

- **API Client Setup**: Configured Anthropic API client with helper functions
- **Message Management**: Functions to add user and assistant messages
- **System Prompts**: Support for system-level instructions
- **Temperature Control**: Adjustable creativity/randomness
- **Streaming**: Real-time response streaming
- **Stop Sequences**: Control when responses end
- **Prompt Evaluation**: Framework for testing and evaluating prompts

## Configuration

The project uses the `claude-haiku-4-5` model by default. You can modify the model in `Int.py`:

```python
model = "claude-haiku-4-5"
```

## Notes

- Make sure your `.env` file is not committed to version control (it's in `.gitignore`)
- The `dataset.json` file contains evaluation test cases for prompt evaluation
- All exercises import functions from `Int.py`, so make sure it's in the root directory

## License

[Add your license here]
