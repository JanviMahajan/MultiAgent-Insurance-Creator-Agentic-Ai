import streamlit as st

def show_sidebar():
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}

    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        padding-top: 20px;
    }

    .sidebar-title {
        font-size: 22px;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
    }

    .stSidebar .stButton button {
        width: 100%;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #1e293b;
        color: white;
        border: none;
        text-align: left;
    }

    .stSidebar .stButton button:hover {
        background-color: #2563eb;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.markdown('<div class="sidebar-title">InsuranceAI</div>', unsafe_allow_html=True)

    if st.sidebar.button("Home"):
        st.switch_page("app.py")

    if st.sidebar.button("Chatbot"):
        st.switch_page("pages/1_Analysis.py")

    if st.sidebar.button("History"):
        st.switch_page("pages/2_History.py")