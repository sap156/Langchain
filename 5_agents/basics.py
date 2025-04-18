# Import required libraries and modules
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's GPT models
from dotenv import load_dotenv  # For loading environment variables
from langchain_core.prompts import PromptTemplate  # For creating prompt templates
from langchain.schema.output_parser import StrOutputParser  # For parsing string outputs
from langchain import hub  # For accessing LangChain's prompt hub
from langchain.agents import create_react_agent, AgentExecutor  # For creating and executing agents
import datetime  # For handling date and time
from langchain.agents import tool  # Decorator to create tools for agents

# Load environment variables (like OPENAI_API_KEY)
load_dotenv()

# Define a custom tool that the agent can use
@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time

# Initialize the language model with gpt-3.5-turbo
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Define the query to be processed by the agent
query = "What is the current time in India? (You are in Central USA). Just show the current time and not the date"

# Pull the ReAct prompt template from LangChain's hub
# This template provides the structure for the agent's reasoning process
prompt_template = hub.pull("hwchase17/react")

'''

hwchase17/react is a prompt template for the REACT agent.
It is used to create a prompt for the agent to follow when answering questions.
It includes the following sections:

Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
'''

# Define the list of tools available to the agent
tools = [get_system_time]

# Create a ReAct agent with the specified LLM, tools, and prompt template
agent = create_react_agent(llm, tools, prompt_template)

# Create an agent executor that will run the agent with the specified tools
# verbose=True enables detailed logging of the agent's thought process
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute the agent with the input query
agent_executor.invoke({"input": query})

