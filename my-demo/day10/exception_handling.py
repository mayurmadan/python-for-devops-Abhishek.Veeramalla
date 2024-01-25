folder_lists = input("please enter the list of folder with spaces between them:").split()
#below print is optional for check 
#print(folder_lists)

import os
def list_files():
    for folders in folder_lists:
        #in case of entering two folder /xyz /home, here /xyz n/a, so it should give o/p for /home
        try:
            file = os.listdir(folders)
            print(f"list of files from folder:- {folders}")
            print(file)
        except FileNotFoundError:
            print(f"provide valid folder name looks like {folders} folder does not exits")
        #in case of permission issue for folder list
        except PermissionError:
             print (f"you dont have permission to list {folders} folder need root user")
        continue    

list_files()

