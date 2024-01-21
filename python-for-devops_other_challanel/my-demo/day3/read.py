#store content in varibale/object
#functioned used open, read, close, readline, readlines
file_content = open("test.txt" , "r")
#file_print = file_content.read() 
#print(file_print)

###########
#IMP
#<><><> we cannot use read & realine &readlines together <><><><>
###########
#to read single line use readline
#line = file_content.readline()
#print(line)

#to read all line use readlines
lines = file_content.readlines()
print(lines)

#now close the open file using close function use this to close file after reading
file_content.close()
