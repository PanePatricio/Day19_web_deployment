FILEPATH=r"todos.txt"
#FILEPATH=r"D:\Python\Tutorials\Udemy\python_mega_course\2023_new_course\Day6_App1_working_with_text_files\todos.txt"
#----------function definition----------open file
def get_todos(filepath=FILEPATH):
    #doc string defintion)
    """Read a textfile and return the list of
    to-do items"""
    with open(filepath, 'r') as file_local:
            todos_local=file_local.readlines()
    return todos_local
#--------------------------------------
#print(help(get_todos)) #docstring function

#----------function definition----------write to file
def write_todos(todos_arg, filepath=FILEPATH):
        """Write the to do items list in the text file"""
        with open(filepath, 'w') as file_local:
            file_local.writelines(todos_arg)
#--------------------------------------
