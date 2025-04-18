# Import required libraries
import os  # For file and directory operations
from langchain.text_splitter import CharacterTextSplitter  # For splitting text into chunks
from langchain_community.document_loaders import TextLoader  # For loading text documents
from langchain_chroma import Chroma  # Vector store for document embeddings
from langchain_openai import OpenAIEmbeddings  # For creating text embeddings

# Define file paths and directories
# Get the current directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))
# Path to the source text file
file_path = os.path.join(current_dir, "documents", "bahubali.txt")
# Directory where the vector store will be saved
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

# Check if vector store exists to avoid recreating it
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Validate source file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please check the path."
        )

    # Load the document using TextLoader
    loader = TextLoader(file_path)
    documents = loader.load()

    # Split the document into smaller chunks for processing
    # chunk_size: number of characters in each chunk
    # chunk_overlap: number of characters that overlap between chunks 
    # This helps in maintaining context between chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50) 
    docs = text_splitter.split_documents(documents)

    # Print information about the chunking process
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings using OpenAI's API
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )  # Using OpenAI's text embedding model
    print("\n--- Finished creating embeddings ---")

    # Initialize Chroma vector store with document embeddings
    print("\n--- Creating vector store ---")
    db = Chroma.from_documents(
        docs,  # Document chunks
        embeddings,  # Embedding model
        persist_directory=persistent_directory  # Where to save the vector store
    )
    print("\n--- Finished creating vector store ---")

else:
    print("Vector store already exists. No need to initialize.")

# Example questions that can be asked about the text
# Who is Devasena?
# Where does Bahubali meet Avantika?