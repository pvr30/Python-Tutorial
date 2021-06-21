# first method
#import modules.file_operation

#file_operation.save_to_file('Vishal', "data.txt")

# second method

from modules.file_operation import read_from_file, save_to_file

save_to_file("Parmar",'data.txt')

print(read_from_file("data.txt"))

# Here Our file_operation file is in modules directory so we need to allow to python
# by modules.file_operation