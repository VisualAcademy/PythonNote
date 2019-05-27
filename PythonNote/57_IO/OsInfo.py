# Environment 
import os

print(os.name)

# FileInfo DirectoryInfo
from os import path

print("FileExists: " + str(path.exists("C:\\temp\\a.txt")))
print("File?: " + str(path.isfile("C:\\temp\\a.txt")))
print("Directory?: " + str(path.isdir("C:\\temp\\a.txt")))

