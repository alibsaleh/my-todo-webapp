FILEPATH = "todos.txt"


def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of
    to do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Write the to-do items list in the text file"""
    #default paramaters NEVER come first when there are multiple arguments
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello World!")
# text = """
# Hi
# Ali
# """
# print(text)

#we can use """ to write paragraphs and long text as it is without using breaklines

