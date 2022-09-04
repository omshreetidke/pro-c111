import os
import shutil


from_dir = "C:\Users\OM\Desktop\pro 111 dup1"
to_dir = "C:\Users\OM\Desktop\pro 111 dup2"

listoffiles = os.listdir(from_dir)
#print(listoffiles)

for filename in listoffiles:

    name, extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
