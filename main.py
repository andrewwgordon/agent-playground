
# Import asyncio for running asynchronous functions
import asyncio
# Import ChatAgent for creating custom agents
from agent_framework import ChatAgent
# Import OpenAIChatClient for OpenAI-based chat agents
from agent_framework.openai import OpenAIChatClient
# Import message and content classes for structured chat messages
from agent_framework import ChatMessage, TextContent, UriContent, Role
# Annotated and Field are used for type-annotated tool definitions
from typing import Annotated
from pydantic import Field


def get_weather(
    location: Annotated[str, Field(description="The location to get weather for")]
) -> str:
    """
    Tool function to get the weather for a given location.
    In a real implementation, this would call a weather API.
    """
    # Your weather API implementation here
    return f"The weather in {location} is sunny with 25°C."


async def tools_example():
    """
    Example of using a ChatAgent with a custom tool (get_weather).
    The agent is instructed to act as a weather assistant and can call the get_weather tool.
    """
    agent = ChatAgent(
        chat_client=OpenAIChatClient(),
        instructions="You are a helpful weather assistant.",
        tools=get_weather,  # Add tools to the agent
    )

    # Ask the agent for the weather in Tokyo; the agent may call the tool
    result = await agent.run("What's the weather like in Tokyo?")
    print(result.text)


async def basic_example():
    """
    Basic example of creating and running an OpenAI-powered chat agent.
    The agent is given a name and instructions, and responds to a simple greeting.
    """
    # Create an agent using OpenAI ChatCompletion
    agent = OpenAIChatClient().create_agent(
        name="HelpfulAssistant",
        instructions="You are a helpful assistant.",
    )

    # Run the agent with a user message
    result = await agent.run("Hello, how can you help me?")
    print(result.text)


async def streaming_example():
    """
    Example of streaming responses from the agent as they are generated.
    The agent is instructed to tell a creative story, and the output is streamed chunk by chunk.
    """
    agent = OpenAIChatClient().create_agent(
        name="StoryTeller",
        instructions="You are a creative storyteller.",
    )

    print("Assistant: ", end="", flush=True)
    # Stream the response as it is generated
    async for chunk in agent.run_stream("Tell me a short story about AI."):
        if chunk.text:
            print(chunk.text, end="", flush=True)
    print()  # New line after streaming


async def joke_example():
    """
    Example of sending a multimodal message (text + image) to the agent.
    The agent is instructed to tell a joke about the provided image.
    """
    agent = OpenAIChatClient().create_agent(
        name="Joker",
        instructions="You are good at telling jokes.",
    )
    # Create a message with both text and an image URI
    message = ChatMessage(
        role=Role.USER, 
        contents=[
            TextContent(text="Tell me a joke about this image?"),
            UriContent(
                uri="https://i.guim.co.uk/img/static/sys-images/Guardian/About/General/2014/1/6/1389022652032/RELIANT-ROBIN-CAR---1990-008.jpg?width=620&dpr=1&s=none&crop=none",
                media_type="image/jpeg"
            )
        ]
    )   
    # Stream the agent's response as it generates the joke
    async for update in agent.run_stream(message):
        if update.text:
            print(update.text, end="", flush=True)
    print() 


async def part_example():
    """
    Example of sending a technical image to the agent for expert analysis.
    The agent is instructed to provide a detailed description of a mechanical part drawing.
    """
    agent = OpenAIChatClient().create_agent(
        name="PartExpert",
        instructions="You are an expert in analysing mechanical part drawings.",
    )
    # Create a message with a prompt and an image URI
    message = ChatMessage(
        role=Role.USER, 
        contents=[
            TextContent(text="Provide a detailed description of this part."),
            UriContent(
                uri="https://cdn.cadcrowd.com/3d-models/85/e7/85e7ddca-5bbc-4bde-9eec-e264ffb48146/gallery/a02211d6-663d-4041-890a-7442cbb67365/medium.jpg",
                media_type="image/jpeg"
            )
        ]
    )   
    # Stream the agent's expert analysis as it is generated
    async for update in agent.run_stream(message):
        if update.text:
            print(update.text, end="", flush=True)
    print() 


# Entry point for running examples
if __name__ == "__main__":
    # Uncomment the example you want to run:
    # asyncio.run(basic_example())        # Run the basic chat example
    # asyncio.run(tools_example())        # Run the tool-using agent example
    # asyncio.run(streaming_example())    # Run the streaming response example
    # asyncio.run(joke_example())         # Run the multimodal joke example
    asyncio.run(part_example())           # Run the mechanical part analysis example