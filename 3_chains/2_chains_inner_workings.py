# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from langchain.prompts import ChatPromptTemplate  # For creating chat prompt templates
from langchain.schema.runnable import RunnableLambda, RunnableSequence  # For creating custom chain components
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize the ChatOpenAI model with GPT-3.5 Turbo
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt templates using ChatPromptTemplate
# Creates a structured format for prompts with variable placeholders
prompt_template = ChatPromptTemplate.from_messages(
     [
        # System message sets the AI's role and context
        ("system", "You love facts and you tell facts about {animal}"),
        # Human message contains the specific request
        ("human", "Tell me {count} facts."),
    ]
)

# Create individual runnables (steps in the chain)
# Step 1: Format the prompt using input variables
format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
# Step 2: Send formatted prompt to the model and get response
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
# Step 3: Extract the content from the model's response
parse_output = RunnableLambda(lambda x: x.content)

# Create the RunnableSequence by combining all steps
# This is equivalent to using the | operator in LCEL
chain = RunnableSequence(
    first=format_prompt,  # First step: format the prompt
    middle=[invoke_model],  # Middle step(s): invoke the model
    last=parse_output  # Last step: parse the output
)

# Execute the chain with specific input values
response = chain.invoke({"animal": "elephant", "count": 2})

# Display the final result
print(response)