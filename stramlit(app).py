import streamlit as st
import time as t
#st.image("hardik.jpeg")
st.title("Python web app development")
st.header("Machine learning")
st.subheader("Linear regression")
st.info("Navya made it")
st.warning("Learn it early")
st.error("go back")
st.write("Navya")
st.success("hurray")
st.markdown("# Movies")
st.markdown("## Movies")
st.markdown(":girl:")
st.caption("Hello")
st.text("Python")
st.latex(r''' a+b x^2+c''')
st.checkbox("Login")
st.button("click")
st.radio("Pick gender",['male','female','other'])
st.selectbox("Pick your choice",['genre','user','ratings'])
st.multiselect("Choose the year",[2020,2021,2023,2024])
st.select_slider("it",['sde1','sde2','sde'])
st.slider("Enter ur age",21,28)
st.number_input("Class",1,12)
st.text_input("Enter ur Email address",)
st.date_input("Date")
st.time_input("time")
st.text_area("Submit ur query")
st.file_uploader("File Uploader mechanism")
st.progress(90)
with st.spinner("Running"):
    t.sleep(2)
st.balloons()
st.sidebar.title("User")
st.sidebar.text_input("Mail Address")
st.sidebar.text_input("password")
st.sidebar.button("Save")
import pandas as pd
import numpy as np
st.title("Bar Chart")
data=pd.DataFrame(np.random.randn(50,2),columns=['x','y'])
st.bar_chart(data)