# agent-playground

## Overview

**agent-playground** is a Python project demonstrating how to build and interact with advanced AI chat agents using the Microsoft `agent-framework` library and OpenAI models. The project provides several example scripts that showcase:
- Basic conversational agents
- Tool-using agents (e.g., weather assistant)
- Streaming responses
- Multimodal input (text + images)
- Technical image analysis

This playground is ideal for developers looking to experiment with or extend AI agent capabilities in Python.

## Getting Started

### Prerequisites
- Python 3.12 or newer
- An OpenAI API key (for OpenAI-powered agents)

### Installation
1. Clone this repository:
   ```bash
   git clone <repo-url>
   cd agent-playground
   ```
2. Install dependencies (using your preferred tool, e.g. pip or uv):
   ```bash
   pip install -r requirements.txt
   # or, if using uv:
   uv pip install --system
   ```
   The main dependency is `agent-framework`.

3. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=your-key-here
   export OPENAI_CHAT_MODEL_ID=gpt-4o-mini
   ```

### Running Examples
Edit `main.py` and uncomment the example you want to run at the bottom of the file. Then run:
```bash
python main.py
```

## How it Works

The core logic is in `main.py`, which contains several example functions:

- **basic_example**: Runs a simple chat agent that responds to greetings.
- **tools_example**: Shows how to add a custom tool (e.g., a weather function) that the agent can call.
- **streaming_example**: Demonstrates streaming agent responses chunk by chunk for real-time output.
- **joke_example**: Sends both text and an image to the agent, which responds with a joke about the image.
- **part_example**: Sends a technical image to the agent for expert analysis and a detailed description.

Each example creates an agent with specific instructions and demonstrates different capabilities of the `agent-framework` library, including tool use, multimodal input, and streaming output.

## Customization
- You can add your own tools by defining Python functions and passing them to the agent.
- Modify the agent's instructions to change its behavior or expertise.
- Extend the examples to suit your use case or integrate with other APIs.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.