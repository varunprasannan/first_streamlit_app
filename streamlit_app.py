import streamlit as st
import snowflake.connector

st.title("My Parent's new Healthy Diner")
st.header("Breakfast Menu")
st.text("🍞Dosa")
st.text("🐔Idli")
st.text("🥣Fruit Salad")
 
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)


import requests
st.header("Fruityvice Fruit Advice!")
fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)


# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

add_my_fruit = st.text_input('What fruit would you like to add?')
st.text("Thanks for adding", add_my_fruit)



