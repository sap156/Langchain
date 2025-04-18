# LangChain Agents

## What are Agents?
Agents in LangChain are autonomous systems that combine Large Language Models (LLMs) with tools to accomplish tasks. They can:
- Make decisions about which tools to use
- Execute multiple steps to solve complex problems
- Handle dynamic situations and unknown tasks
- Learn from interactions and feedback

## How Agents Work

### 1. Decision Making Process
Agents follow the ReAct (Reasoning + Acting) framework:
- **Thought**: Analyze the current situation
- **Action**: Choose and use appropriate tools
- **Observation**: Process results
- **Reflection**: Plan next steps

### 2. Core Components

#### Tools
Tools are functions that agents can use to interact with the world:
```python
@tool
def calculate_area(length: float, width: float) -> float:
    """Calculate area of a rectangle"""
    return length * width
```

#### Memory Systems
- **Short-term**: Current conversation context
- **Long-term**: Persistent storage of information
- **Working Memory**: Temporary task-specific data

#### Planning Systems
- Task decomposition into subtasks
- Goal tracking and validation
- Error handling and recovery

## Types of Agents

### 1. OpenAI Functions Agent
Optimized for function calling with structured outputs:
```python
from langchain.agents import create_openai_functions_agent
agent = create_openai_functions_agent(llm, tools, prompt)
```

### 2. ReAct Agent
Uses reasoning and acting steps explicitly:
```python
from langchain.agents import create_react_agent
agent = create_react_agent(llm, tools, prompt)
```

### 3. Plan-and-Execute Agent
Breaks down complex tasks into structured plans:
```python
from langchain.agents import create_plan_and_execute_agent
agent = create_plan_and_execute_agent(llm, tools, prompt)
```

## Common Use Cases

1. **Research Assistant**
   - Web searching
   - Information synthesis
   - Fact verification

2. **Task Automation**
   - File operations
   - Data processing
   - Scheduling

3. **Interactive Systems**
   - Customer service
   - Educational tutoring
   - Technical support

## Best Practices

### 1. Tool Design
- Clear, specific descriptions
- Input/output validation
- Error handling
- Rate limiting

### 2. Prompt Engineering
- Explicit instructions
- Clear constraints
- Example interactions
- Safety guidelines

### 3. System Design
- Modular tool structure
- Appropriate memory systems
- Logging and monitoring
- Performance optimization

## Limitations

1. **Technical Constraints**
   - Token limits
   - API rate limits
   - Tool complexity

2. **Safety Considerations**
   - Input validation
   - Output sanitization
   - Access control
   - Error handling

3. **Cost Management**
   - API usage monitoring
   - Optimization strategies
   - Caching mechanisms

## Overview
Learn how to create, customize, and deploy LangChain agents for various tasks.

## File Descriptions

### 1. Basic Agents (`1_basics.py`)
- Basic agent setup and configuration
- Tool definition and usage
- ReAct framework implementation
```python
from langchain.agents import create_react_agent, AgentExecutor
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
```

## Agent Components

### 1. Tools
- Built-in tools (search, math, etc.)
- Custom tool creation
- Tool validation and documentation

### 2. Memory
- Short-term memory
- Long-term memory
- Memory types and usage

### 3. Planning
- Task decomposition
- Goal setting
- Progress tracking

## Best Practices
1. Define clear tool descriptions
2. Implement proper error handling
3. Use appropriate agent type for task
4. Monitor token usage
5. Test agent behavior thoroughly

## Example Usage

### Basic Agent with Tools
```python
from langchain_openai import ChatOpenAI
from langchain.agents import tool
from datetime import datetime

@tool
def get_current_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """Returns the current time in specified format"""
    return datetime.now().strftime(format)

llm = ChatOpenAI(model="gpt-4")
tools = [get_current_time]
agent = create_react_agent(llm, tools, prompt_template)
```

### Agent with Multiple Tools
```python
from langchain.agents import load_tools
tools = load_tools(["wikipedia", "python_repl"])
agent = create_react_agent(llm, tools, prompt_template)
```

## Common Use Cases
1. Task automation
2. Information gathering
3. Data analysis
4. Content generation
5. Problem-solving

## Debugging Tips
- Use `verbose=True` for detailed logging
- Monitor tool usage patterns
- Check agent reasoning steps
- Validate tool inputs/outputs

## Additional Resources
- [LangChain Agents Documentation](https://python.langchain.com/docs/modules/agents/)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/gpt/function-calling)
- [ReAct Framework Paper](https://arxiv.org/abs/2210.03629)