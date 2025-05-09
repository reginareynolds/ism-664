# Import libraries
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are an expert in marine biology")

result = Runner.run_sync(agent, "What creature lives the deepest in the ocean, "
                                "and at what depth has it been recorded?")

print(result.final_output.strip())