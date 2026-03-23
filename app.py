import streamlit as st

st.set_page_config(page_title="InsuranceAI", layout="wide")

# 🎨 UI Styling
st.markdown("""
<style>

/* Hide default page navigation */
[data-testid="stSidebarNav"] {display: none;}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
    padding-top: 20px;
}

/* Sidebar title */
.sidebar-title {
    font-size: 22px;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

/* Sidebar buttons */
.stSidebar .stButton button {
    width: 100%;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
    background-color: #1e293b;
    color: white;
    border: none;
    text-align: left;
    font-size: 15px;
}

/* Hover effect */
.stSidebar .stButton button:hover {
    background-color: #2563eb;
    color: white;
}

/* Hero section */
.hero {
    background: linear-gradient(to right, #1e3a8a, #2563eb);
    padding: 40px;
    border-radius: 15px;
    color: white;
    text-align: center;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f1f5f9;
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}
</style>
""", unsafe_allow_html=True)

# 📌 SIDEBAR (CUSTOM TITLE)
st.sidebar.markdown('<div class="sidebar-title">InsuranceAI</div>', unsafe_allow_html=True)

# 📌 SIDEBAR MENU
if st.sidebar.button("Home"):
    st.switch_page("app.py")

if st.sidebar.button("Chatbot"):
    st.switch_page("pages/1_Analysis.py")

if st.sidebar.button("History"):
    st.switch_page("pages/2_History.py")

# 🌟 HERO SECTION
st.markdown('<div class="hero"><h1>InsuranceAI</h1><p>Smart Insurance Analysis using AI</p></div>', unsafe_allow_html=True)

st.write("")

# 🔍 INPUT
st.markdown("### Ask your insurance question")

query = st.text_input("E.g. What is health insurance?")

if st.button("Analyze"):
    if query:
        st.session_state["query"] = query
        st.switch_page("pages/1_Analysis.py")
    else:
        st.warning("Please enter a query")

st.write("")

# 💡 FEATURES
st.markdown("## Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><b>Research Agent</b><br>Finds policy insights</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><b>Writer Agent</b><br>Creates reports</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><b>Smart Insights</b><br>Recommendations</div>', unsafe_allow_html=True)