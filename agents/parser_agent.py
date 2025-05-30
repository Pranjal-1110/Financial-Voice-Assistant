from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from models import parsed_output 

load_dotenv()
    
# Define the prompt template for parsing user queries
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a financial analyst specializing in parsing user queries related to market risks, earnings highlights, macroeconomic updates, and news lookups. \n Your task is to extract structured information from user queries."),
        ("user", "Parse the following user query and extract structured information:\n {query}"),     
    ]
) 

# Initialize the LLM with the structured output
llm = ChatOpenAI(
    model = "gpt-4o-mini",
    temperature = 0.0,
) 

structured_llm = llm.with_structured_output(parsed_output, method= "function_calling")


# Function to parse user queries using the defined prompt and LLM
def get_parsed_output(query: str) -> parsed_output:
    
    """
    Parses the user query to extract structured information.
    
    Args:
        query (str): The user query to be parsed.
        
    Returns:
        parsed_output: A structured output containing parsed information.
    """
    
    chain = prompt_template | structured_llm
    result = chain.invoke({"query": query})
    
    if isinstance(result, dict):
        result = parsed_output(**result)
        
    return result
    
    

    
    
    
    