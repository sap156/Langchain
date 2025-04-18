# LangChain Chat Models Examples

This directory contains examples of working with various chat models through LangChain's unified interface.

## Overview
Learn how to interact with different Language Models (LLMs), manage conversations, handle chat history, and implement persistence.

## Setup
1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages:
```bash
pip install langchain langchain-openai python-dotenv firebase-admin
```

3. Set up environment variables in `.env`:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

## File Descriptions

### 1. Basic Chat Model Usage (`1_chat_models_starter.py`)
- Basic initialization of ChatOpenAI
- Simple query/response interaction
- Error handling and response parsing
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4")
result = llm.invoke("What is LangChain?")
```

### 2. Managing Conversations (`2_chat_models_conversation.py`)
- Using different message types (System, Human, AI)
- Building multi-turn conversations
- Managing conversation context
```python
messages = [
    SystemMessage(content="You are an expert in Python."),
    HumanMessage(content="Explain decorators.")
]
```

### 3. Alternative Models (`3_chat_models_alternative_models.py`)
- Integration with Google's Gemini
- Using Anthropic's Claude
- Comparing model capabilities
- Model selection strategies

### 4. Interactive Chat (`4_chat_model_conversation_with_user.py`)
- Building interactive chat applications
- Managing user input/output
- Handling conversation flow
- Exit conditions and error handling

### 5. Firebase Integration (`5_chat_model_save_message_history_firebase.py`)
- Setting up Firebase for chat history
- Implementing persistence
- Managing chat sessions
- Retrieving historical conversations

## Usage Examples

### Basic Query
```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4")
response = llm.invoke("Explain LangChain in one sentence.")
print(response.content)
```

### Conversation with History
```python
from langchain.schema import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is RAG?")
]
response = llm.invoke(messages)
```

## Best Practices
1. Always use environment variables for API keys
2. Implement proper error handling
3. Consider token usage and costs
4. Use appropriate model for the task
5. Implement rate limiting for production use

## Troubleshooting
- Check API key configuration
- Verify network connectivity
- Monitor rate limits
- Check model availability

## Additional Resources
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction.html)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Firebase Setup Guide](https://firebase.google.com/docs/web/setup)