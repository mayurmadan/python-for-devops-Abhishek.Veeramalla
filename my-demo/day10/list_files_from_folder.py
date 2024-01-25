folder_lists = input("please enter the list of folder with spaces between them:").split()
print(folder_lists)

import os
def list_files():
    for folders in folder_lists:        
#        print(folders)
        print("=====list of files from folder-",folders)
        #here listdir is like ls -a & provide o/p as a list, so we convert it into proper o/p using below step of for loop
        file_list = os.listdir(folders)

        for files in file_list:
            print(files)

list_files()
