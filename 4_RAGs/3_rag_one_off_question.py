import os

from dotenv import load_dotenv  # For loading environment variables
from langchain_chroma import Chroma  # Vector store for document embeddings
from langchain_core.messages import HumanMessage, SystemMessage  # Message types for chat
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # OpenAI models

# Load environment variables from .env (including OPENAI_API_KEY)
load_dotenv()

# Define the persistent directory where the vector store is located
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(
    current_dir, "db", "chroma_db_with_metadata")

# Initialize the embedding model (using the cost-effective small model)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load the existing vector store with the embedding function
# This allows us to search through previously embedded documents
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Define the user's question about Dracula
query = "What does dracula fear the most?"

# Set up document retrieval parameters
retriever = db.as_retriever(
    search_type="similarity",  # Use basic similarity search
    search_kwargs={"k": 3},    # Retrieve top 3 most relevant documents
)
# Perform the search and get relevant documents
relevant_docs = retriever.invoke(query)

# Display the retrieved documents
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")

# Prepare the prompt by combining:
# 1. The original question
# 2. Retrieved relevant documents
# 3. Instructions for the model
combined_input = (
    "Here are some documents that might help answer the question: "
    + query
    + "\n\nRelevant Documents:\n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    + "\n\nPlease provide a rough answer based only on the provided documents. If the answer is not found in the documents, respond with 'I'm not sure'."
)

# Initialize the GPT-4 model for generating responses
model = ChatOpenAI(model="gpt-4")

# Prepare the chat messages
messages = [
    SystemMessage(content="You are a helpful assistant."),  # Set AI's role
    HumanMessage(content=combined_input),  # Provide the query and context
]

# Send the messages to the model and get response
result = model.invoke(messages)

# Display the generated response
print("\n--- Generated Response ---")
print("Content only:")
print(result.content)

# Note: This implementation demonstrates a basic RAG system:
# 1. Takes a user question
# 2. Finds relevant documents using vector similarity
# 3. Combines question and documents into a prompt
# 4. Uses GPT-4 to generate an informed answer