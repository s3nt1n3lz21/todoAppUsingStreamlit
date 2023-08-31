FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]


def write_todos(todos, filepath=FILEPATH):
    todos = [todo + '\n' for todo in todos]
    with open(filepath, 'w') as file:
        file.writelines(todos)
