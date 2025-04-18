# Import required libraries
from dotenv import load_dotenv  # For loading environment variables
from langchain.prompts import ChatPromptTemplate  # For creating chat prompt templates
from langchain.schema.runnable import RunnableLambda, RunnableParallel  # For parallel processing
from langchain.schema.output_parser import StrOutputParser  # For parsing string output
from langchain_openai import ChatOpenAI  # For interacting with OpenAI's chat models

# Load environment variables (including OPENAI_API_KEY)
load_dotenv()

# Initialize ChatOpenAI model with GPT-3.5 Turbo
model = ChatOpenAI(model="gpt-4")

# Define initial prompt template for getting movie summary
summary_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a movie critic."),
        ("human", "Provide a brief summary of the movie {movie_name}."),
    ]
)

# Define function for plot analysis
def analyze_plot(plot):
    # Create template for plot analysis
    plot_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the plot: {plot}. What are its strengths and weaknesses?"),
        ]
    )
    # Format the prompt with the provided plot
    return plot_template.format_prompt(plot=plot)

# Define function for character analysis
def analyze_characters(characters):
    # Create template for character analysis
    character_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a movie critic."),
            ("human", "Analyze the characters: {characters}. What are their strengths and weaknesses?"),
        ]
    )
    # Format the prompt with the provided characters
    return character_template.format_prompt(characters=characters)

# Function to combine the separate analyses into a final report
def combine_verdicts(plot_analysis, character_analysis):
    return f"Plot Analysis:\n{plot_analysis}\n\nCharacter Analysis:\n{character_analysis}"

# Create individual analysis chains using LCEL
# Plot analysis branch: analyze plot -> get model response -> parse to string
plot_branch_chain = (
    RunnableLambda(lambda x: analyze_plot(x)) | model | StrOutputParser()
)

# Character analysis branch: analyze characters -> get model response -> parse to string
character_branch_chain = (
    RunnableLambda(lambda x: analyze_characters(x)) | model | StrOutputParser()
)

# Create the complete parallel processing chain:
# 1. Get movie summary
# 2. Process plot and character analyses in parallel
# 3. Combine results into final verdict
chain = (
    summary_template  # Start with movie summary template
    | model  # Get summary from model
    | StrOutputParser()  # Parse to string
    | RunnableParallel(branches={  # Run analyses in parallel
        "plot": plot_branch_chain,
        "characters": character_branch_chain
    })
    | RunnableLambda(lambda x: combine_verdicts(  # Combine results
        x["branches"]["plot"],
        x["branches"]["characters"]
    ))
)

# Execute the chain with a specific movie
result = chain.invoke({"movie_name": "Inception"})

# Display the final analysis
print(result)