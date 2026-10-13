import os
from groq import Groq
import streamlit as st

def get_groq_client():
    try:
        api_key = st.secrets["groq_api_key"]
    except Exception:
        api_key = os.environ.get("GROQ_API_KEY", "")
    return Groq(api_key=api_key)

def run_agent_query(agent_name, prompt):
    client = get_groq_client()
    
    # Quetta Safe City official accurate roads and infrastructure context
    quetta_context = """
    Context about Quetta Safe City:
    - Accurate Main Roads in Quetta: Jinnah Road, Saryab Road, Shahrah-e-Zarghoon (Zarghoon Road), Brewery Road, Samungli Road, Airport Road, Liaquat Bazaar, Mezan Chowk.
    - Infrastructure: 200+ PTZ Cameras, 1000+ Fixed Cameras, 30+ ANPR Units.
    - Provide realistic, accurate real-time-like situational analysis based strictly on Quetta's actual geography and official infrastructure. Do not invent fake road names like Mardan Road or Kalat Road.
    """
    
    system_prompts = {
        "Traffic & ANPR Agent": f"You are a specialized AI agent for Quetta Safe City monitoring ANPR, multi-lane traffic, and vehicle recognition systems on actual Quetta roads. {quetta_context}",
        "Emergency Response Agent": f"You are an emergency response coordination agent handling PTZ camera feeds, crime alerts, and quick incident management in Quetta's real localities. {quetta_context}",
        "System Health Agent": f"You are a system health and admin analytics agent tracking server logs, IoT sensor networks, and overall dashboard status for Quetta Safe City. {quetta_context}"
    }
    
    full_prompt = f"User Request: {prompt}\n\nPlease provide accurate real-time analysis using Quetta's authentic locations and infrastructure."
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompts.get(agent_name, "You are a helpful assistant.")},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.5,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"
