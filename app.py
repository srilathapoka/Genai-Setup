import google.generativeai as genai
import os
import streamlit as st

#get api from local env
key=os.getenv('GOOGLE_API_KEY')

#configure the model
genai.configure(api_key=key)
model=genai.GenerativeModel('gemini-2.5-flash-lite')

#create a frontend UI
st.title('SIMPLE TEXT GENERATION')
st.header('this to test the gemini model as application')
prompt=st.text_input('write your prompt',max_chars=1000)
if prompt:
    response=model.generate_content(prompt)
    st.write(response.text)