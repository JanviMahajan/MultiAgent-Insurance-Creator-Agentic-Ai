import streamlit as st
import json

st.title("History")

try:
    with open("data/history.json", "r") as f:
        data = json.load(f)

    for item in reversed(data):
        st.markdown("### " + item["query"])
        st.write(item["report"])
        st.markdown("---")

except:
    st.info("No history yet")