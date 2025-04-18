# Import required libraries
import os  # For file and directory operations
from langchain.text_splitter import CharacterTextSplitter  # For splitting text into chunks
from langchain_community.document_loaders import TextLoader  # For loading text files
from langchain_community.vectorstores import Chroma  # Vector store with metadata support
from langchain_openai import OpenAIEmbeddings  # For creating text embeddings

# Set up directory structure
current_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
books_dir = os.path.join(current_dir, "documents")  # Directory containing source text files
db_dir = os.path.join(current_dir, "db")  # Base directory for database storage
persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")  # Vector store location

# Display directory paths for verification
print(f"Books directory: {books_dir}")
print(f"Persistent directory: {persistent_directory}")

# Check if vector store exists to avoid reprocessing
if not os.path.exists(persistent_directory):
    print("Persistent directory does not exist. Initializing vector store...")

    # Validate source directory exists
    if not os.path.exists(books_dir):
        raise FileNotFoundError(
            f"The directory {books_dir} does not exist. Please check the path."
        )

    # Get list of all .txt files in the books directory
    book_files = [f for f in os.listdir(books_dir) if f.endswith(".txt")]

    # Process each book file and add metadata
    documents = []
    for book_file in book_files:
        # Construct full path to the book file
        file_path = os.path.join(books_dir, book_file)
        # Load the text content
        loader = TextLoader(file_path)
        book_docs = loader.load()
        # Add metadata to each document chunk
        for doc in book_docs:
            doc.metadata = {"source": book_file}  # Track which file each chunk came from
            documents.append(doc)

    # Split documents into smaller chunks for processing
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,  # Number of characters per chunk
        chunk_overlap=0   # No overlap between chunks
    )
    docs = text_splitter.split_documents(documents)

    # Display processing information
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")

    # Initialize embedding model
    print("\n--- Creating embeddings ---")
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"  # Using OpenAI's smaller embedding model
    )
    print("\n--- Finished creating embeddings ---")

    # Create and persist the vector store
    print("\n--- Creating and persisting vector store ---")
    db = Chroma.from_documents(
        docs,                           # Document chunks with metadata
        embeddings,                     # Embedding model
        persist_directory=persistent_directory  # Where to save the vector store
    )
    print("\n--- Finished creating and persisting vector store ---")

else:
    print("Vector store already exists. No need to initialize.")

# Note: This script processes multiple text files and maintains source tracking
# through metadata. The resulting vector store can be queried to find relevant
# text chunks along with their source documents.