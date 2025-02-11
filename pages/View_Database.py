import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from FoodTracker.DB import DatabaseManager as DM

#set page configuration
st.set_page_config(layout="wide")

#get required data from database
all_data,daily_data,today_data = DM.fetch_all_meals()

st.title("This is what you have eaten so far")

col1,col2=st.columns(2)

with col1:
    st.write("### Entire database")
    st.dataframe(all_data,hide_index=True)

with col2:
    st.write("### Daily database")
    st.dataframe(daily_data,hide_index=True)
    st.write("### What have I Eaten today")
    st.dataframe(today_data,hide_index=True)