import os 
#input_folder_list = input("enter the folder list with space:").split()
#print(input_folder_list)

#create function 
def list_files(input_folder_list):
    for folders in input_folder_list:
        #use os module 
        try:
            files = os.listdir(folders)
            print(f"list of files from {folders} folder:")
            for files_name in files:
                print(files_name)
        except FileNotFoundError: #this error name we get from cli when same senario happen , this should be same
            print(f"provide valid folder name looks like {folders} folder does not exits")
        except PermissionError:
             print (f"you dont have permission to list {folders} folder need root user")
             continue
        
#sample function 2
def hello(name):
    print("my name is:", name)

