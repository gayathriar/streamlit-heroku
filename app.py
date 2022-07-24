import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Multiply two numbers

This app multiplies two numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    number1 = st.number_input("Fist Number",min_value=0,max_value=2000000)
    number2 = st.number_input("Second Number",min_value=0,max_value=2000000)
    
df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())

#Preprocessing




product = number1 * number2


st.subheader('Results of multiplication')
st.write(product)
