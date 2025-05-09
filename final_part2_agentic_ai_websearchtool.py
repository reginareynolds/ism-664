# Import libraries
import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Try importing agent-related modules
try:
  from agents import Agent, Runner, WebSearchTool, trace
except ImportError:
  st.error("The required 'agents' module or related tools are missing. Ensure all dependencies are installed.")
  st.stop()  # Stop execution due to missing dependency

# Define async function to fetch updates based on city and topic
async def get_web_search_update(city, topic):
  """
  Async function to run the agent and fetch the web search result for a specific city and topic.
  """

  agent = Agent(name="Web searcher",
                instructions="You are a helpful agent",
                tools=[WebSearchTool(user_location={"type": "approximate", "city": city})]
  )

  with trace("Web search example"):
    result = await Runner.run(agent, f"Search the web for '{topic} news in {city}' and give me 3 "
                                     f"interesting updates in a sentence."
    )

  return result.final_output


# Set up UI frontend using Streamlit
st.title("Web Search: OpenAI Agent Interface")
st.write("This application uses an OpenAI Agent to fetch **specific updates** by city and topic.")

with st.form("city_topic_form"):
  st.text("Please enter only a city name and a topic word to fetch the update using agentic web search.")
  user_city = st.text_input("Enter a city name:", placeholder="e.g., Greensboro, Melbourne, London")
  user_topic = st.text_input("Enter a news topic:", placeholder="e.g., politics, weather, sports")
  submitted = st.form_submit_button("Submit")

  if submitted:
    if user_city.strip() == "" or user_topic.strip() == "" :
      st.error("Please enter both a valid city and a topic.")
    else:
      st.info(f"Fetching **{user_topic} update** for **{user_city}**... Please wait.")

      # Safely run the async function
      try:
        # Pass user entered city and topic
        result = asyncio.run(get_web_search_update(user_city, user_topic))
        st.success(f"Here are the interesting updates for **{user_city}**:")
        st.markdown(f"**{result}**")  # Format the result to display nicely
      except Exception as e:
        st.error(f"An error occured while fetching the updates: {e}")

# Footer section
st.write("---")
st.caption("Powered by OpenAI Agent")
