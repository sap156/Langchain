# Import required libraries
import os  # For file and directory operations
from langchain_chroma import Chroma  # Vector store for document embeddings
from langchain_openai import OpenAIEmbeddings  # For creating text embeddings
from langchain_openai import ChatOpenAI  # For chat completions
from langchain.schema import HumanMessage, SystemMessage  # Message types for chat

# Set up directory paths
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
db_dir = os.path.join(current_dir, "db")  # Database directory
persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")  # Vector store location

# Initialize the embedding model
# Using the smaller, cost-effective embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load the existing vector store
# embedding_function is required to convert new queries into vectors
db = Chroma(persist_directory=persistent_directory,
            embedding_function=embeddings)

# Define the search query
query = "Where is Dracula's castle located?"

# Set up the retriever with specific search parameters
retriever = db.as_retriever(
    search_type="similarity_score_threshold",  # Use similarity scoring
    search_kwargs={
        "k": 3,  # Return top 3 matches
        "score_threshold": 0.2,  # Include documents with 20% or higher similarity
    },
)

# Perform the search and get relevant documents
relevant_docs = retriever.invoke(query)

# Display search results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    print(f"Source: {doc.metadata['source']}\n")

# The following section is for RAG (Retrieval Augmented Generation)
# Currently commented out but demonstrates how to:
# 1. Combine retrieved documents with the query
# 2. Use ChatGPT to generate a response based on the documents

'''
# Prepare the combined input for the LLM
combined_input = (
    "Here are some documents that might help answer the question: "
    + query
    + "\n\nRelevant Documents:\n"
    + "\n\n".join([doc.page_content for doc in relevant_docs])
    + "\n\nPlease provide a rough answer based only on the provided documents. "
    + "If the answer is not found in the documents, respond with 'I'm not sure'."
)

# Initialize the ChatGPT model
model = ChatOpenAI(model="gpt-4")

# Prepare the chat messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=combined_input),
]

# Get the model's response
result = model.invoke(messages)

# Display the results
print("\n--- Generated Response ---")
print("Content only:")
print(result.content)
'''