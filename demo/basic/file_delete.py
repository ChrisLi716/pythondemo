# coding=utf-8

import os

currentPath = os.getcwd()
print("currentPath", currentPath, sep=":")

newDirPath = currentPath + os.sep + "tmp" + os.sep


def create_dir_if_not_exist():
    if not os.path.exists(newDirPath):
        os.mkdir(newDirPath)
    else:
        print(newDirPath, "has existed!")


def write2file(file_path: list, content):
    for fpath in file_path:
        try:
            if not os.path.exists(fpath):
                # "x" - 创建 - 将创建一个文件，如果文件存在则返回错误
                file = open(fpath, "x")
            else:
                file = open(fpath, "w")
                print(fpath, "has existed!")
                file.write(content)
        finally:
            file.close()


def del_file(file_path):
    is_del = input("are your sure to delete file : " + file_path + "[Y / N]?")
    if is_del == "Y" or is_del == "y":
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            print("quit delete!")
    else:
        print(file_path, "doesn't exist!")


def read_file():
    f = open(demo1)
    print(f.read())


create_dir_if_not_exist()

# create file and write content
demo1 = newDirPath + "demo1.txt"
demo2 = newDirPath + "demo2.txt"
demo3 = newDirPath + "demo3.txt"
write2file([demo1, demo2, demo3], "for testing purpose!")

# read file
read_file()

# del_file()
