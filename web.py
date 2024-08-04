import streamlit as st
import functions_web

todos = functions_web.read_todos()
# getting the existing list of to-dos


def add_todo():
    if st.session_state['new_todo'] != '':
        # we do this so that the function does not
        # add anything new if the input is empty
        to_do = st.session_state["new_todo"] + "\n"
        # new_todo will be key of the session state dict,
        # and it will hold the value to_do, which is the user input
        # Note:
        # 'session_state' is used to store and manage user-specific data that persists
        # across interactions with the app during a single session. In other words, it lets you
        # save information (like user choices or form inputs) so it stays the same
        # even when the app updates. It behaves like a dictionary, and it will contain
        # pairs of data that the user enters on the app while interacting with it

        todos.append(to_do)
        # appending new to-dos to the list
        functions_web.write_todos(todos)
        # writing the updated to-do list in todos.txt file


# removing the user input from the input box after it is added
st.session_state["new_todo"] = ""

# the order in which we write these lines of code/functions, will reflect on our web page
# for e.g. if the st.title() is written at the third line of code, then in the web page,
# the main title will be in the third line
st.title("My To-do App")
st.subheader("This is a to-do app for managing daily tasks")
st.write("Use this app to save time and increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.capitalize(), key=todo)
    if checkbox:
        todos.pop(index)
        functions_web.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new to-do item...",
              on_change=add_todo, key='new_todo')

st.session_state
