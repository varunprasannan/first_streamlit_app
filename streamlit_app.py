import streamlit as st

st.title("My Parent's new Healthy Diner")
st.header("Breakfast Menu")
st.text("🍞Dosa")
st.text("🐔Idli")
st.text("🥣Fruit Salad")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
