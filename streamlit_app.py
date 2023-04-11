import streamlit as st
import pandas as pd

st.title('My Parents Happy Diner')

st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = st.multiselect('Pick some Fruits:', list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc(fruits_selected)

st.dataframe(fruits_to_show)
