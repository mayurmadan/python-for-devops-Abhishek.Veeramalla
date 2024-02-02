#https://github.com/mayurmadan/python-for-devops-Abhishek.Veeramalla/tree/main/python-for-devops_other_challanel/my-demo/day3

#open file in read mode
file_content = open("test_module.py", "r")

#now reading all content from file 
line =  file_content.readline()
print(line)

#now open file to write using write mode
file_content = open("test_module.py", "w")

file_content.write("this is new line added2")
file_content = open("test_module.py", "r")

lines = file_content.readline()
print(lines)

#now close the file mode using
file_content.close()

