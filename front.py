import streamlit as st
import datetime
st.title("To-Do List")

st.sidebar.write("User Authentication")

username=st.sidebar.text_input('Username')

password=st.sidebar.text_input('Password',type="password")

if st.sidebar.checkbox('Submit'):
    menu=["Create Task", "Read Task", "Update task", "Delete task"]
    option = st.selectbox(
    "Menu",
    menu, index=None,)
    if (option == 'Create Task'):
        #database shit
        task = st.text_input('Name of task')
        completion_date = st.date_input("When's your task due", datetime.date(2019, 7, 6))
    elif (option == 'Read Task'):
        st.write("database daalo")
    elif(option == 'Update Task'):
        st.write("dsfdsf")

