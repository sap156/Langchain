# Import the ChatOpenAI class from langchain_openai for interacting with OpenAI's chat models
from langchain_openai import ChatOpenAI
# Import load_dotenv to load environment variables from .env file
from dotenv import load_dotenv

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize the language model
# Using GPT-3.5-turbo model which is optimized for chat/conversation
llm = ChatOpenAI(
    model="gpt-3.5-turbo")

# Send a query to the model and get the response
# The invoke method sends a single message and returns the model's response
result = llm.invoke("What is the capital of USA?")

# Print the content of the response
# The content attribute contains the actual text response from the model
print(result.content)

