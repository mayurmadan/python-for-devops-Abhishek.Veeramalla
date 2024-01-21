#functioned used open funtion with write mode 
#this is use to write in file store in file-content varibale [it override existing content as we use write mode]
file_content = open("test.txt" , "w")
file_content.write("this is new line\n")

file_content.close()
