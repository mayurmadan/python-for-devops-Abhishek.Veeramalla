#module used here is os, os.path, time, shutil
#OS module is used to interact with operating system 
import os

#create folder using same module
os.mkdir('test1')

#list content from currnt dir 
a = os.listdir(".")
print(a)

#check file or folder exit or not
import os.path
b = os.path.exists("test.txt")
print ("check the above file is present or not:", b)

#to add sleep
import time
# Sleep for 5 seconds
time.sleep(5)

#remove folder 
os.rmdir("test1")
c = os.listdir("/home/mayur-test")
print(c)

#remove file 
os.remove("mayur.txt")
print(os.listdir("."))

#remove folder contain file or subfolder(recursivily)
import shutil
shutil.rmtree("/home/mayur-test/mayur")

