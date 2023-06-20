import streamlit as st

st.title("My Parent's new Healthy Diner")
st.header("Breakfast Menu")
st.text("🍞Dosa")
st.text("🐔Idli")
st.text("🥣Fruit Salad")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

st.dataframe(my_fruit_list)


