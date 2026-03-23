from utils.groq_api import call_llm

def research_agent(query):
    prompt = f"""
    You are an insurance expert.
    Explain clearly:

    {query}

    Include:
    - Definition
    - Types
    - Benefits
    """
    return call_llm(prompt)