import os
from groq import Groq

def get_groq_client(api_key):
    return Groq(api_key=api_key)

def run_agent_query(api_key, agent_name, prompt):
    if not api_key:
        return "Barah-e-karam apni Groq API Key enter karein."
    
    client = get_groq_client(api_key)
    
    system_prompts = {
        "Traffic & ANPR Agent": "You are a specialized AI agent for Quetta Safe City monitoring ANPR, multi-lane traffic, and vehicle recognition systems.",
        "Emergency Response Agent": "You are an emergency response coordination agent handling PTZ camera feeds, crime alerts, and quick incident management in Quetta.",
        "System Health Agent": "You are a system health and admin analytics agent tracking server logs, IoT sensor networks, and overall dashboard status for Quetta Safe City."
    }
    
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompts.get(agent_name, "You are a helpful assistant.")},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"
