import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['add_todo']
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=i)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state['add_todo']
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='add_todo')

