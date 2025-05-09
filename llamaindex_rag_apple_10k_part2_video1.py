# Import libraries
import os
import streamlit as st
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
llama_api_key = os.getenv("LLAMAINDEX_API_KEY")

from llama_index.indices.managed.llama_cloud import LlamaCloudIndex
# pip install llama-index-indices-managed-llama-cloud

# Connect to LlamaCloud using Llama API key
index = LlamaCloudIndex(
  name="apple-rag-10k-token-chunks",
  project_name="Default",
  organization_id="bd02aa26-bf2a-49e5-869e-41dc1b36a493",
  api_key=llama_api_key,
)


# Function to generate response using queried input
def generate_response(input_text):
  query_response = index.as_query_engine().query(input_text)

  # Return the response from the LLM
  return str(query_response)


def generate_response_nodes(input_text):
  nodes = index.as_retriever().retrieve(input_text)
  return str(nodes)


# Set up UI frontend using Streamlit
with st.form("OpenAI and LLAMAINDEX POWERED FINANCIAL ANALYST LLM ASSISTANT USING RAG AND STREAMLIT FOR UI"):
  st.header("OpenAI and LLAMAINDEX Powered Financial Analyst LLM Assistant")
  st.subheader("Using RAG for Company Data and Streamlit for User Interface")

  # User input section
  user_input = st.text_area("Enter your financial questions about Apple's 10K filings for the 2023 and 2024 fiscal years -- Your query goes here")
  submitted = st.form_submit_button("Submit")

  if submitted:
    if user_input:
      # Generate a new response
      response = generate_response(user_input)

      # Display the user input and LLM response in the main content area
      st.subheader("Your question:")
      st.write(user_input)

      st.subheader("Response:")
      st.info(response)

    else:
      st.warning("Please enter a query to submit.")
