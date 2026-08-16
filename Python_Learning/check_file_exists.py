# METHOD 1 => os.path.exist()
import os

file_name = "practice.txt"
# file_name = "C:/Users/HP/PycharmProjects/PythonProject/Python_Learning/practice.txt" # replace \ with /
if os.path.exists(file_name):
    print("File exists")
else:
    print("File does not exist")

# METHOD 2 => pathlib.Path.exists()
from pathlib import Path

file_name_2 = Path("C:/Users/HP/PycharmProjects/PythonProject/Python_Learning/practice.txt")

if file_name_2.exists():
    print("File already exists")
else:
    print("File does not exist, creating file")
    fh = open(file_name_2, "xt")
    fh.write("Hello World")
    fh.close()
