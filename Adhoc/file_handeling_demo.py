import os

# def read_file(file_path):
#     if file_path is None:
#         return False
#     if not os.path.exists(file_path):
#         return False
#
#     file = open(file_path, 'r')
#     content = file.readline()
#     print(content)
#     content = file.readlines()
#     print(content)
#
#     file.seek(0)
#
#     content = file.readlines()
#     print(content)
#
#     file.close()
#     return True
#
#
# def write_file(file_path,data,encodeing='utf-8'):
#     """
#
#     :param file_path:
#     :param data:
#     :return:
#     If file exists it is going to overwrite it; previous data will be lost.
#     If file does not exist then a new file will be created.
#     """
#     file = open(file_path,'w')
#     file.write(data)
#     file.write('End of file')
#     file.close()
#
#
# file_path = 'write_demo.txt'
# write_file(file_path,"Hello world")
#
#
# def append_file(file_path,data):
#     file = open(file_path,'a')
#     file.write(data)
#     file.close()
#
# file_path = 'write_demo.txt'
# append_file(file_path,"new data for appending")



# def append_file(file_path,data):
#     file = open(file_path,'a')
#     file.write(data)
#     file.close()
#
# file_path = 'write_demo.txt'
# append_file(file_path,"new data for appending")




















