# backend to the web.py file

FILEPATH = "todos_web.txt"


def read_todos(filepath=FILEPATH):
    """ Reads the existing to-to items from the todos_web.txt text file. """
    # Docstring document what this function does :0
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
        return todo_list_local


def write_todos(todo_list_arg, filepath=FILEPATH):
    # the correct format is non-default parameter followed by default parameter
    """ Writes to-do items in the todos_web.txt text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todo_list_arg)


# print("Hello from functions")
# the point to writing this line is to show that when
# we import this module in main.py, and then execute main.py
# this script in the functions_web.py also gets executed
# due to the 'from functions import read_todos, write_todos' (or 'import functions') line
# written in the main.py file

# if we don't want print("Hello from functions") to be executed when we run
# the main.py file, we can do this:

if __name__ == "__main__":
    print("This line won't be executed when we run main.py")


