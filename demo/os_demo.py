import os

# 用于在文件中分隔行的字符串
print(os.linesep)
# 用来分隔文件路径名的字符串
print(os.sep)
# 用于分隔文件路径的字符串
print(os.pathsep)
# 当前工作目录的字符串名称
print(os.curdir)
# (当前工作目录的)父目录字符串名称
print(os.pardir)

# os.walk 函数可以得到一个三元tupple(dirpath, dirnames, filenames).
for root, dirs, files in os.walk(os.getcwd() + os.sep + "tmp"):
    print(root)  # 当前目录路径
    print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件

full_name_list = []
for root, dirs, files in os.walk(os.getcwd() + os.sep + "tmp"):
    for file in files:
        tuple_file = os.path.splitext(file)
        print(tuple_file[0], tuple_file[1], sep="")
        full_name_list.append(os.path.join(root, file))

print(full_name_list)


# os.listdir()函数得到的是仅当前路径下的文件名，不包括子目录中的文件，所有需要使用递归的方法得到全部文件名
def list_dir_files(path, file_name_list: list):
    for file_tmp in os.listdir(path):
        file_path = os.path.join(path, file_tmp)
        if os.path.isdir(file_path):
            list_dir_files(file_path, file_name_list)
        else:
            file_name_list.append(file_path)
    return file_name_list


current_file_path = os.getcwd()
list_name = list()
for one_file_full_name in list_dir_files(current_file_path, list_name):
    print(one_file_full_name)
