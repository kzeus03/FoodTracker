import streamlit as st

st.title("Welcome to Food Tracker")
st.write("### Select the service you want")

# Ensure files are inside the 'pages/' directory
st.page_link("pages/CalorieTracker.py", label="Calorie Tracker")
st.page_link("pages/AddFood.py", label="Add Food")
st.page_link("pages/View_Database.py",label="View Database")
