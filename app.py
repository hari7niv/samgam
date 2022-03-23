import streamlit as st
import sqlite3 
connection = sqlite3.connect('name.db')
name = st.selectbox('name',['','Athavan(Don)','Shailesh','Aravinth(Pus)','Hari'])
text = st.text_input('content')
button = st.button('post') 
if button:
          connection.execute(f"INSERT INTO san VALUES ('{text}','{name}')")
          cursor = connection.execute("SELECT * from san ")
          for row in cursor:
               st.subheader(row[1])
               st.write(row[0])

