import streamlit as st

st.set_page_config(page_title = "Scrape2Insights", layout = "wide")
st.title("Scrape2Insights")
st.caption("Tech News and Finance in Crypto - MVP Dashboard")

tab1, tab2 = st.tabs(["Insights", "Operations"])
with tab1:
    st.write("Coming soon: Top News, price charts, filters")

with tab2:
    st.write("Coming soon: Job status, last run, basic health")

