# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from google.cloud import firestore  # Firebase Firestore client
from langchain_google_firestore import FirestoreChatMessageHistory  # For storing chat history in Firestore
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models

"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project and FireStore Database
3. Retrieve the Project ID
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    - Set your default project to the new Firebase project you created
5. pip install langchain-google-firestore
6. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com&project=crewai-automation
"""

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Setup Firebase Firestore configuration
PROJECT_ID = "langchain-a5989"  # Your Firebase project ID
SESSION_ID = "user_session_new"  # Unique identifier for the chat session
COLLECTION_NAME = "chat_history"  # Firestore collection name for storing messages

# Initialize Firestore Client with project ID
print("Initializing Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History with session details
print("Initializing Firestore Chat Message History...")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)
print("Chat History Initialized.")
print("Current Chat History:", chat_history.messages)

# Initialize the OpenAI chat model
model = ChatOpenAI()

print("Start chatting with the AI. Type 'exit' to quit.")

# Main chat loop
while True:
    # Get user input
    human_input = input("User: ")
    if human_input.lower() == "exit":
        break

    # Add user message to chat history
    chat_history.add_user_message(human_input)

    # Get AI response using the entire chat history
    ai_response = model.invoke(chat_history.messages)
    # Store AI response in chat history
    chat_history.add_ai_message(ai_response.content)

    # Display AI response
    print(f"AI: {ai_response.content}")