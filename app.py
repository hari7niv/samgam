import streamlit as st
import sqlite3 
connection = sqlite3.connect('app.db')
c = connection.cursor()
name = st.selectbox('name',['','Athavan(Don)','Shailesh','Aravinth(Puspa)','Hari'])
text = st.text_input('content')
button = st.button('post')


if button:
     c.execute(f"INSERT INTO san VALUES ('{text}','{name}')")
     connection.commit()


c.execute("SELECT * from san ")
i = c.fetchall()

for row in i:
    st.subheader(row[1])
    st.write(row[0])

delt = st.button("clear all")
if delt:
    connection.execute('DELETE FROM san')
    connection.commit()

