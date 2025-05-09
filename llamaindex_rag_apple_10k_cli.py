# Import libraries
import os
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

# Create query
query = ("You are an expert business analyst. What was the difference between Apple's projected 2024 earnings "
         "versus their actual earnings? What events may have contributed to this difference?")

# Interface with LlamaIndex
nodes = index.as_retriever().retrieve(query)
response = index.as_query_engine().query(query)

# Print the response from the LLM
print(response)
