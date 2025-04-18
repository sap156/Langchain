# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from langchain.prompts import ChatPromptTemplate  # For creating chat prompt templates
from langchain.schema.output_parser import StrOutputParser  # For parsing output as string
from langchain.schema.runnable import RunnableLambda  # For creating custom chain components
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize the ChatOpenAI model with GPT-3.5 Turbo
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define the first prompt template for generating animal facts
animal_facts_template = ChatPromptTemplate.from_messages(
    [
        # System message sets the AI's role as a fact teller
        ("system", "You like telling facts and you tell facts about {animal}."),
        # Human message requests specific number of facts
        ("human", "Tell me {count} facts."),
    ]
)

# Define a second prompt template for translation to French
translation_template = ChatPromptTemplate.from_messages(
    [
        # System message sets the AI's role as a translator
        ("system", "You are a translator and convert the provided text into {language}."),
        # Human message provides text for translation
        ("human", "Translate the following text to {language}: {text}"),
    ]
)

# Define additional processing steps using RunnableLambda
# Count words in the text and prepend the count to the text
count_words = RunnableLambda(lambda x: f"Word count: {len(x.split())}\n{x}")
# Prepare the output for translation by formatting it as input for translation template
prepare_for_translation = RunnableLambda(lambda output: {"text": output, "language": "spanish"})

# Create the combined chain using LangChain Expression Language (LCEL)
# The chain flows as follows:
# 1. animal_facts_template: Format the initial prompt
# 2. model: Generate animal facts
# 3. StrOutputParser: Convert to string
# 4. prepare_for_translation: Format for translation
# 5. translation_template: Format translation prompt
# 6. model: Translate the text
# 7. StrOutputParser: Convert final output to string
chain = animal_facts_template | model | StrOutputParser() | prepare_for_translation | translation_template | model | StrOutputParser() 

# Execute the chain with input parameters
result = chain.invoke({"animal": "elephant", "count": 2})

# Display the final translated output
print(result)