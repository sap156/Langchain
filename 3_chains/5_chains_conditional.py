# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from langchain.prompts import ChatPromptTemplate  # For creating chat prompt templates
from langchain.schema.output_parser import StrOutputParser  # For parsing string output
from langchain.schema.runnable import RunnableBranch  # For conditional branching
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model instance
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt templates for different types of feedback responses
# Template for positive feedback - generates thank you notes
positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a thank you note for this positive feedback: {feedback}."),
    ]
)

# Template for negative feedback - generates apologetic responses
negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Generate a response addressing this negative feedback: {feedback}."),
    ]
)

# Template for neutral feedback - asks for more details
neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a request for more details for this neutral feedback: {feedback}.",
        ),
    ]
)

# Template for cases requiring escalation to human agent
escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        (
            "human",
            "Generate a message to escalate this feedback to a human agent: {feedback}.",
        ),
    ]
)

# Template for classifying feedback sentiment
classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human",
         "Classify the sentiment of this feedback as positive, negative, neutral, or escalate: {feedback}."),
    ]
)

# Define conditional branches for different feedback types
branches = RunnableBranch(
    # Branch 1: Handle positive feedback
    (
        lambda x: "positive" in x,  # Condition for positive feedback
        positive_feedback_template | model | StrOutputParser()  # Chain for positive feedback
    ),
    # Branch 2: Handle negative feedback
    (
        lambda x: "negative" in x,  # Condition for negative feedback
        negative_feedback_template | model | StrOutputParser()  # Chain for negative feedback
    ),
    # Branch 3: Handle neutral feedback
    (
        lambda x: "neutral" in x,  # Condition for neutral feedback
        neutral_feedback_template | model | StrOutputParser()  # Chain for neutral feedback
    ),
    # Default branch: Escalate to human agent
    escalate_feedback_template | model | StrOutputParser()
)

# Create the classification chain
classification_chain = classification_template | model | StrOutputParser()

# Combine classification and response generation into one chain
# First classifies the feedback, then routes to appropriate response branch
chain = classification_chain | branches

# Example usage with different types of feedback
# Good review - "The product is excellent. I really enjoyed using it and found it very helpful."
# Bad review - "The product is terrible. It broke after just one use and the quality is very poor."
# Neutral review - "The product is okay. It works as expected but nothing exceptional."
# Default - "I'm not sure about the product yet. Can you tell me more about its features and benefits?"

# Test the chain with a negative review
review = "The product is terrible. It broke after just one use and the quality is very poor."
result = chain.invoke({"feedback": review})

# Output the generated response
print(result)