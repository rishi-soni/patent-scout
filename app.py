import streamlit as st
from dotenv import load_dotenv
from agent.agent import build_agent

load_dotenv()

st.set_page_config(page_title="PatentScout", page_icon="🔬")
st.title("🔬 PatentScout")
st.caption("Turn thousands of patents into one actionable insight.")

query = st.text_input(
    "Enter a biotech AI topic:",
    placeholder="e.g. AI diagnostics for rare diseases"
)

if st.button("Find White Spaces →"):
    if not query:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Agent is searching and analyzing patents..."):
            agent = build_agent()
            result = agent.invoke({"input": f"Find white spaces in biotech AI patents related to: {query}"})
            st.markdown(result["output"])
