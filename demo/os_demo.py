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

for root, dirs, files in os.walk(os.getcwd()):
    print(root)  # 当前目录路径
    print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件
