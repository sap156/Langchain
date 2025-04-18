# Import specific message types for different roles in the conversation
from langchain_core.messages import SystemMessage , HumanMessage, AIMessage
# Import ChatOpenAI for interacting with OpenAI's chat models
from langchain_openai import ChatOpenAI
# Import load_dotenv to load environment variables
from dotenv import load_dotenv

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize the language model with GPT-3.5-turbo
llm = ChatOpenAI(
    model="gpt-3.5-turbo")

# Create a list of messages to simulate a conversation
# SystemMessage: Sets the behavior/role of the AI
# HumanMessage: Represents user input
messages = [
    SystemMessage(content="You are an expert in soical media content strategy."),
    HumanMessage(content="Give a short tip to improve my Medium blog post visibility."),
]

# Send the conversation messages to the model and get response
result = llm.invoke(messages)
# Print the AI's response
print(result.content)