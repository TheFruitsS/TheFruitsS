from os import path
from os import linesep
#file = open('/home/dimitarvili/Downloads/VioletaProjects/PythonAdvanced/File Handling/FileHandling_exercise/venv/demo')

#print(file)
# rarely you can work with this path
#print(path.abspath('.')) #mostly you will work this way so if you deploy the program so and others can use it the program will work on the other this way
file_path = './output.txt'
with open(file_path, 'a') as file:
    file.write('Jesus' + linesep)
