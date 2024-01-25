import test_module

input_folder_list = ["/root","/xyz","/opt","/home"]
name = input(str("enter your name:"))
test_module.list_files(input_folder_list)
test_module.hello(name)

