# LangChain Chains

## What are Chains?
Chains in LangChain are sequences of operations that combine different components to create complex workflows. They allow you to:
- Connect multiple LLM calls together
- Combine LLMs with other tools and utilities
- Create reusable pipelines for common tasks
- Handle complex logic and data transformations

## Types of Chains

### 1. Simple Chains
The most basic type that connects a prompt template to an LLM:
```python
template | model | output_parser
```

### 2. Sequential Chains
Connect multiple operations in sequence, where output of one feeds into the next:
```python
first_chain = template1 | model  # Summarize text
second_chain = template2 | model # Translate summary
full_chain = first_chain | second_chain
```

### 3. Parallel Chains
Execute multiple operations concurrently and combine their results:
```python
parallel_chain = RunnableParallel(
    summary=summarize_chain,
    analysis=analyze_chain,
    translation=translate_chain
)
```

### 4. Conditional Chains
Route to different chains based on conditions:
```python
chain = RunnableBranch(
    (lambda x: x["length"] > 100, summarize_chain),
    (lambda x: x["language"] != "english", translate_chain),
    default_chain
)
```

## Chain Components
1. **Prompt Templates**: Define input structure
2. **LLMs**: Process inputs and generate outputs
3. **Output Parsers**: Format and structure outputs
4. **Tools**: Additional utilities and functions
5. **Memory**: Store and retrieve context

## Benefits of Using Chains
1. **Modularity**: Easy to compose and modify
2. **Reusability**: Create once, use many times
3. **Maintainability**: Clear structure and flow
4. **Scalability**: Handle complex workflows
5. **Flexibility**: Mix and match components

## Overview
LangChain chains combine multiple components (prompts, models, other chains) into unified workflows.

## File Descriptions

### 1. Basic Chains (`1_chains_basics.py`)
- Simple chain construction
- LCEL (LangChain Expression Language) basics
- Basic chain operations
```python
from langchain_core.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_template("tell me a {adjective} joke about {topic}")
chain = template | model | output_parser
```

### 2. Chain Internals (`2_chains_inner_workings.py`)
- Chain components and structure
- Custom chain creation
- Chain debugging and monitoring
- Memory management

### 3. Sequential Chains (`3_chains_sequential.py`)
- Multiple steps in sequence
- Data passing between steps
- Error handling in sequences
```python
first_chain = template1 | model | parser
second_chain = template2 | model | parser
full_chain = first_chain | second_chain
```

### 4. Parallel Chains (`4_chains_parallel.py`)
- Concurrent processing
- Result aggregation
- Resource management
```python
from langchain.schema.runnable import RunnableParallel
parallel_chain = RunnableParallel(
    summary=summary_chain,
    analysis=analysis_chain
)
```

### 5. Conditional Chains (`5_chains_conditional.py`)
- Branch handling
- Decision making
- Route selection
```python
from langchain.schema.runnable import RunnableBranch
chain = RunnableBranch(
    (lambda x: condition, first_chain),
    (lambda x: other_condition, second_chain),
    default_chain
)
```

## Common Chain Types

### 1. LLM Chain
- Single prompt -> LLM -> output
- Basic text generation and transformation

### 2. Sequential Chain
- Multiple steps in sequence
- Output of one step feeds into next

### 3. Router Chain
- Dynamic routing based on input
- Multiple possible paths

### 4. Transform Chain
- Data preprocessing
- Output formatting

## Best Practices
1. Use LCEL for modern chain construction
2. Implement proper error handling
3. Monitor token usage
4. Test chains with various inputs
5. Consider chain reusability

## Debugging Tips
- Use `verbose=True` in chain creation
- Implement callbacks for monitoring
- Test components individually
- Check input/output formats

## Performance Optimization
1. Batch processing when possible
2. Proper caching configuration
3. Resource cleanup
4. Concurrent execution when appropriate

## Example Usage

### Basic Chain
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

model = ChatOpenAI()
template = ChatPromptTemplate.from_template("Explain {concept}")
chain = template | model

result = chain.invoke({"concept": "LangChain chains"})
```

### Sequential Chain
```python
summarize = template1 | model
translate = template2 | model
chain = summarize | translate

result = chain.invoke({"text": "long text here"})
```

## Additional Resources
- [LangChain Chains Documentation](https://python.langchain.com/docs/modules/chains/)
- [LCEL Guide](https://python.langchain.com/docs/expression_language/)
- [Chain Examples Repository](https://github.com/langchain-ai/langchain/tree/master/templates)