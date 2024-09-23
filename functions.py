import functions

FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        newtodo = file_local.readlines()
        return newtodo


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def complete_todos(index, filepath=FILEPATH):
    todos = functions.get_todos()
    todos.pop(index)
    functions.write_todos(todos)