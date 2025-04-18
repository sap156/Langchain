# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from langchain.prompts import ChatPromptTemplate  # For creating structured chat prompts
from langchain.schema.output_parser import StrOutputParser  # For parsing output as string
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models

# Load environment variables (including OPENAI_API_KEY) from .env file
load_dotenv()

# Initialize the ChatOpenAI model with GPT-4
model = ChatOpenAI(model="gpt-4o")

# Define prompt templates using ChatPromptTemplate
# This creates a structured format for our prompts with variable placeholders
prompt_template = ChatPromptTemplate.from_messages(
    [
        # System message defines the AI's role and context
        ("system", "You are a facts expert who knows facts about {animal}."),
        # Human message contains the specific request
        ("human", "Tell me {fact_count} facts."),
    ]
)

# Create the chain using LangChain Expression Language (LCEL)
# The | operator creates a sequential chain where:
# 1. prompt_template formats the input
# 2. model generates the response
# 3. StrOutputParser converts the response to a string
chain = prompt_template | model | StrOutputParser()
# Alternative without string parsing: chain = prompt_template | model

# Execute the chain with specific input values
result = chain.invoke({"animal": "elephant", "fact_count": 1})

# Display the result
print(result)