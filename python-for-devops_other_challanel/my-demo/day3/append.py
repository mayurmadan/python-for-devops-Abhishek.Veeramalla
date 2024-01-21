#this is use to write in file store in file-content varibale [it append into existing content as we use append mode]
file_content2 = open("test.txt","a")
file_content2.write("\n\nthis is append content2\n")
print(file_content2)

file_content2.close()
print(file_content2)
