# LangChain Tutorial

## What is LangChain?
LangChain is a framework for developing applications powered by language models. It provides:
- Unified interface to various LLMs (GPT-4, Claude, etc.)
- Tools for prompt management and optimization
- Chains for complex task orchestration
- Agents for autonomous decision-making
- Memory systems for context management
- Document handling and RAG capabilities

## Repository Structure
```
LangChain/
├── 1_chat_models/         # Chat model implementations
├── 2_prompt_templates/    # Prompt engineering examples
├── 3_chains/              # Chain implementations
├── 4_RAGs/                # Retrieval Augmented Generation
├── 5_agents/              # Agent implementations
└── requirements.txt       # Project dependencies
```

## Setup and Installation

### Prerequisites
- Python 3.9 or higher
- OpenAI API key
- (Optional) Firebase account for chat history persistence

### Environment Setup
1. Clone the repository:
```bash
git clone <https://github.com/sap156/Langchain.git>
cd Langchain
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
.env
# Edit .env and add your OpenAI API key
```

## Module Descriptions

### 1. Chat Models (`1_chat_models/`)
- Basic chat model usage
- Conversation management
- Message history
- Firebase integration

### 2. Prompt Templates (`2_prompt_templates/`)
- Basic templating
- Dynamic prompts
- Message-based templates
- Template validation

### 3. Chains (`3_chains/`)
- Sequential chains
- Parallel processing
- Conditional branching
- Custom chain creation

### 4. RAG Systems (`4_RAGs/`)
- Document processing
- Vector stores
- Similarity search
- Question answering

### 5. Agents (`5_agents/`)
- Tool definition
- Agent types
- Multi-agent systems
- Custom tools

## Best Practices
1. Always use environment variables for API keys
2. Implement proper error handling
3. Monitor token usage and costs
4. Test extensively with different inputs
5. Follow rate limiting guidelines

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Troubleshooting
- Check API key configuration
- Verify environment activation
- Monitor rate limits
- Check model availability

## Additional Resources
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI Documentation](https://platform.openai.com/docs/introduction)
- [Vector Store Guide](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
- [Agent Development](https://python.langchain.com/docs/modules/agents/)

## Contact
For questions and support, please open an issue in the repository.