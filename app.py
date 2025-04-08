import streamlit as st
import joblib
import sklearn

st.title(" Rain fall Prediction")

a1 = st.number_input("enter cloud : ")
a2 = st.number_input("enter pressure : ")
a3 = st.number_input("enter humidity : ")
a4 = st.number_input("enter sunshine : ")
a5 = st.number_input("enter winddirection : ")
a6 = st.number_input("enter dewpoint : ")
a7 = st.number_input("enter windspeed : ")
 
if st.button ("predict"):
    op=mymodel.predict([[a1,a2,a3,a4,a5,a6,a7]])
   
       