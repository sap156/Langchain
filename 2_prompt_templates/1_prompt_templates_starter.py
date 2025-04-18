# Import required libraries
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models
from dotenv import load_dotenv  # For loading environment variables
from langchain_core.prompts import ChatPromptTemplate  # For creating structured chat prompts

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize the ChatOpenAI model with GPT-3.5 Turbo
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Example 1: Simple Template (Currently commented out)
# Define a template for job application emails with variable placeholders
template = "Write a {tone} email to {company} expressing interest in the {position} position, mentioning {skill} as a key strength. Keep it to 4 lines max"

# Create a ChatPromptTemplate from the template string
prompt_template = ChatPromptTemplate.from_template(template)
print(prompt_template) # Print the prompt template to see its structure

# Invoke the template with specific values
prompt =  prompt_template.invoke({
     "tone": "energetic", 
     "company": "OpenAI", 
     "position": "AI Data Engineer", 
     "skill": "Data Engineering"
 })

# Example 2: Prompt with System and Human Messages
# Define messages as tuples with role and content
#messages = [
#    ("system", "You are a comedian who tells jokes about {topic}."),  # System message sets AI's role
#    ("human", "Tell me {joke_count} jokes."),  # Human message contains the request
#]

# Create a prompt template from the messages
#prompt_template = ChatPromptTemplate.from_messages(messages)

# Invoke the template with specific values for topic and joke count
#prompt = prompt_template.invoke({"topic": "lawyers", "joke_count": 3})

# Send the formatted prompt to the language model and get response
result = llm.invoke(prompt)

# Display the AI's response
print(result.content)
