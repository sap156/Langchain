# Retrieval Augmented Generation (RAG) Examples

This folder contains examples of implementing RAG systems using LangChain. RAG combines document retrieval with language model generation to provide accurate, context-aware responses.

## What is RAG?
Retrieval Augmented Generation (RAG) is an AI architecture that enhances Large Language Models (LLMs) by:
- Retrieving relevant information from a knowledge base (external data source like a vector database)
- Incorporating this information into the prompt
- Generating responses based on both the retrieved context and the model's training
- Reducing hallucinations by grounding responses in specific documents

## Key Components

### Vector Databases
Vector databases are specialized databases that store and search high-dimensional vectors. They:
- Store document embeddings efficiently
- Enable similarity search operations
- Support fast nearest neighbor searches
- Persist data for repeated use
- Examples: Chroma, Pinecone, Weaviate


### Embeddings
Embeddings are numerical representations of text that:
- Capture semantic meaning in vector form
- Allow for similarity comparisons
- Convert text into fixed-size vectors
- Preserve relationships between similar concepts
- Enable efficient document retrieval

More on Vector Databases and Embeddings Explained Simply :(https://medium.com/gopenai/vector-databases-and-embeddings-explained-like-youre-15-5d23879fea05)

## Files Structure

### Basic RAG Implementation
- `1a_basic_part_1.py` - Document loading and embedding setup
- `1b_basic_part_2.py` - Basic document retrieval and querying

### RAG with Metadata
- `2a_rag_basics_metadata.py` - Document processing with metadata tracking
- `2b_rag_basics_metadata.py` - Retrieval with metadata and response generation

### Advanced RAG Features
- `3_rag_one_off_question.py` - Single question answering with RAG

## How RAG Works
1. Document Processing:
   - Text documents are split into chunks
   - Each chunk is converted to an embedding vector
   - Vectors are stored in a vector database

2. Query Processing:
   - User question is converted to an embedding
   - Similar documents are retrieved from vector DB
   - Retrieved context is combined with the question
   - LLM generates answer using this enhanced context

## Setup Requirements
1. Create a `documents` folder and add your text files
2. Ensure OpenAI API key is set in `.env`
3. Install required packages:
```bash
pip install langchain langchain-openai chromadb
```

## Usage Examples

### Loading Documents
```python
python3 1a_basic_part_1.py
```

### Querying Documents
```python
python3 1b_basic_part_2.py
```

## Directory Structure
```
4_RAGs/
├── documents/           # Source text files
├── db/                 # Vector store databases
│   ├── chroma_db/     # Basic vector store
│   └── chroma_db_with_metadata/  # Vector store with metadata
└── *.py               # Python implementation files
```

## Best Practices
1. Document Chunking:
   - Choose appropriate chunk sizes
   - Use meaningful overlap between chunks
   - Maintain document context

2. Embedding Selection:
   - Use consistent embedding models
   - Consider cost vs. performance
   - Monitor embedding quality

3. Vector Store Management:
   - Implement proper persistence
   - Regular maintenance and updates
   - Monitor storage requirements

## Notes
- Vector stores are persisted to avoid reprocessing
- Uses OpenAI's text-embedding-3-small for cost-effective embeddings
- Implements various retrieval strategies (similarity, threshold-based)

## Additional Resources
- [Understanding RAG Systems](https://python.langchain.com/docs/modules/data_connection/)
- [Vector Databases Explained](https://www.pinecone.io/learn/vector-database/)
- [Embedding Models Guide](https://platform.openai.com/docs/guides/embeddings)