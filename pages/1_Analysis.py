import streamlit as st
from agents.researcher import research_agent
from agents.writer import writer_agent
import json
import os
from utils.sidebar import show_sidebar

st.set_page_config(layout="wide")

# ✅ Sidebar
show_sidebar()

# 🎨 Styling
st.markdown("""
<style>
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f1f5f9;
    margin-bottom: 15px;
}
.suggestion {
    background-color: #e0e7ff;
    padding: 8px 12px;
    border-radius: 8px;
    margin: 5px;
    display: inline-block;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

st.title("Chatbot")

# 💡 Suggested Questions
st.subheader("💡 Try these:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("What is health insurance?"):
        st.session_state["query"] = "What is health insurance?"

with col2:
    if st.button("Best insurance for family?"):
        st.session_state["query"] = "Best insurance for family?"

with col3:
    if st.button("How to claim insurance?"):
        st.session_state["query"] = "How to claim insurance?"

st.write("")

# 📌 Input
query = st.session_state.get("query", "")
query = st.text_input("Ask your insurance question", value=query)

# 💾 Ensure history
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/history.json"):
    with open("data/history.json", "w") as f:
        json.dump([], f)

# 💾 Save function
def save_history(query, report):
    try:
        with open("data/history.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({"query": query, "report": report})

    with open("data/history.json", "w") as f:
        json.dump(data, f)

# 🚀 Run
if st.button("Run AI Analysis"):

    # 🔍 Research
    with st.spinner("Analyzing..."):
        research = research_agent(query)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Research Output")
    st.write(research)
    st.markdown('</div>', unsafe_allow_html=True)

    # 📝 Writer
    with st.spinner("Generating report..."):
        report = writer_agent(research)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Final Report")
    st.write(report)
    st.markdown('</div>', unsafe_allow_html=True)

    # 💡 SMART SUGGESTIONS
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💡 Suggestions")

    st.success("✔ Compare multiple insurance policies before choosing")
    st.success("✔ Check claim settlement ratio of company")
    st.success("✔ Balance between premium and coverage")
    st.success("✔ Read exclusions carefully before buying")

    st.markdown('</div>', unsafe_allow_html=True)

    # 💾 Save
    save_history(query, report)

    st.success("Saved to history")