from utils.groq_api import call_llm

def writer_agent(research_data):
    prompt = f"""
    Convert this into a clean structured report:

    {research_data}

    Format:
    - Title
    - Summary
    - Key Points
    """
    return call_llm(prompt)