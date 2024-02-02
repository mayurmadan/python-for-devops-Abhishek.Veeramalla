#update server conf file
def update_file_function(file_name,key,value):
    
    #to read each line from file  using read mode
    #here as file  is alias given 
    with open(file_name, "r") as file:
        #store all the read using readline in the variable here 
        lines = file.readlines()
   
   #to write file open it in write mode
    with open(file_name, "w") as file:
        for line in lines:
            if key in line:
                file.write(key +"="+value +"\n")
            else:
                file.write(line)

#now calling function by provideing value for element
update_file_function("server.conf","MAX_CONNECTIONS", "2000")                           



