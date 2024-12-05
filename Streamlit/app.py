import streamlit as st
import pandas as pd
st.title('Practicing Streamlit')
name = st.text_input('Enter your name')
if name:

 st.write(f'The name entered is {name}')

age = st.slider('select age',0,100,18)
st.write(f"the age selected is {age}")

options = ['Javascript','Java','C++','C','Ruby','Python']
lang= st.selectbox('Select your favorite language',options)
st.write(f"your favorite language is {lang}")

data ={
 'name' : ['John' , 'Tom' , ' Serena' ,'Cindy'],
 'age' : [20,30,40,50]
 }

df = pd.DataFrame(data)
st.write(df)
df.to_csv('sampledata.txt')

upoloaded_file = st.file_uploader('Choose the csv file', type = 'csv')
if upoloaded_file:
 data1 = pd.read_csv(upoloaded_file)
 uploaded_dataframe = pd.DataFrame(data1)
 st.write(uploaded_dataframe)
 