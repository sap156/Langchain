# LangChain Prompt Templates

Examples of creating and using prompt templates in LangChain for structured and dynamic prompting.

## Overview
Learn how to create, format, and use different types of prompt templates to improve consistency and reusability in LLM interactions.

## Setup
1. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages:
```bash
pip install langchain langchain-openai python-dotenv
```

3. Configure environment variables in `.env`:
```plaintext
OPENAI_API_KEY=your_api_key_here
```

## File Descriptions

### 1. Basic Templates (`1_prompt_templates_starter.py`)
- Simple string-based templates
- Variable substitution
- Basic formatting options
```python
template = "Write a {tone} email about {topic}"
prompt = ChatPromptTemplate.from_template(template)
```

### 2. Message-Based Templates (`example 2: 1_prompt_templates_starter.py`)
- System and Human message templates
- Role-based prompting
- Multi-turn conversation templates
```python
messages = [
    ("system", "You are an expert in {field}"),
    ("human", "Explain {concept} in simple terms")
]
```

## Usage Examples

### Basic Template
```python
from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in {subject}"),
    ("human", "Explain {concept} to a {level} student")
])

prompt = template.format(
    subject="mathematics",
    concept="calculus",
    level="high school"
)
```

### With LangChain Expression Language (LCEL)
```python
from langchain_openai import ChatOpenAI

chain = template | ChatOpenAI() | StrOutputParser()
result = chain.invoke({
    "subject": "physics",
    "concept": "quantum mechanics",
    "level": "college"
})
```

## Best Practices
1. Use descriptive variable names
2. Include clear instructions in templates
3. Consider context length limits
4. Implement error handling
5. Test templates with various inputs
6. Use type hints when possible

## Template Structure
- System Message: Set context and role
- Human Message: Main query or task
- Variables: Use clear, descriptive names
- Instructions: Be specific and clear

## Common Use Cases
1. Email Generation
2. Code Documentation
3. Tutorial Creation
4. Q&A Systems
5. Content Summarization
6. Format Conversion

## Troubleshooting
- Check variable names match in template and data
- Verify all required variables are provided
- Monitor token usage
- Test edge cases

## Additional Resources
- [LangChain Templates Documentation](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)
- [LCEL Guide](https://python.langchain.com/docs/expression_language/)
- [Best Practices for Prompting](https://platform.openai.com/docs/guides/prompt-engineering)