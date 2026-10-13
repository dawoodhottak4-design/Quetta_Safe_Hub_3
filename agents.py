import os
from groq import Groq
import streamlit as st
from duckduckgo_search import DDGS

def get_groq_client():
    try:
        api_key = st.secrets["groq_api_key"]
    except Exception:
        api_key = os.environ.get("GROQ_API_KEY", "")
    return Groq(api_key=api_key)

def web_search(query):
    """DuckDuckGo se real-time internet search karne ka function"""
    try:
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text(query, max_results=3)]
            return "\n".join(results) if results else "No live search results found."
    except Exception as e:
        return f"Search error: {str(e)}"

def run_agent_query(agent_name, prompt):
    client = get_groq_client()
    
    # Live internet search execution based on user prompt
    search_query = f"Quetta Balochistan {prompt}"
    search_results = web_search(search_query)
    
    quetta_context = f"""
    You are an advanced AI command and control agent for Quetta Safe City (bsca.gov.pk).
    You have performed a live real-time internet search regarding the user's request. 
    Here is the live search data fetched from the internet:
    {search_results}
    
    Use this live data along with official Quetta Safe City infrastructure context (200+ PTZ cameras, 1000+ fixed cameras, 30+ ANPR units on Jinnah Road, Saryab Road, Shahrah-e-Zarghoon) to provide an accurate, real-time status report.
    """
    
    system_prompts = {
        "Traffic & ANPR Agent": f"{quetta_context}\nYour role: Monitor live traffic flow, vehicle recognition, and congestion using real-time search and Quetta infrastructure.",
        "Emergency Response Agent": f"{quetta_context}\nYour role: Handle emergency coordination, PTZ camera feeds, and real-time security alerts in Quetta.",
        "System Health Agent": f"{quetta_context}\nYour role: Track system health, IoT sensors, and admin control room metrics for Quetta Safe City."
    }
    
    full_prompt = f"Live Query: {prompt}\n\nProvide an immediate real-time report based on the live internet search data above:"
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompts.get(agent_name, "You are a helpful assistant.")},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.6,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"
