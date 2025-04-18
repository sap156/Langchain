# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models
from langchain.schema import AIMessage, HumanMessage, SystemMessage  # Message types for conversation

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize the ChatOpenAI model with GPT-4
model = ChatOpenAI(model="gpt-4")

# Initialize an empty list to store the conversation history
chat_history = []  # This will maintain the order of messages between human and AI

# Create and add a system message to set the AI's behavior
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history

# Start an interactive chat loop
while True:
    # Get user input
    query = input("You: ")
    # Check if user wants to exit
    if query.lower() == "exit":
        break
    
    # Add user's message to chat history
    chat_history.append(HumanMessage(content=query))

    # Get AI's response using the entire chat history for context
    result = model.invoke(chat_history)
    response = result.content
    # Add AI's response to chat history
    chat_history.append(AIMessage(content=response))

    # Display AI's response
    print(f"AI: {response}")

# Display the entire conversation history at the end
print("---- Message History ----")
print(chat_history)