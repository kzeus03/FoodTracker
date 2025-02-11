import os
import sys
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from FoodTracker.DB import DatabaseManager as DM
from FoodTracker.pages import CalorieTracker as CalorieTracker


load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROG_API_KEY"), model_name="llama-3.3-70b-versatile")

st.title("My food Database")
food = st.text_input("Enter a food item: ", key="food_input")
if food:
        d = CalorieTracker.get_calories(food)
        st.dataframe(d)
        DM.store_meal_data(food,d)
        st.write("Data stored Successfully")

