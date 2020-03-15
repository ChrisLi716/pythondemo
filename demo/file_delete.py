import os

currentPath = os.getcwd()
print("currentPath", currentPath, sep=":")

newDirPath = currentPath + os.sep + "tmp" + os.sep

try:
    if not os.path.exists(newDirPath):
        os.mkdir(newDirPath)
    else:
        print(newDirPath, "has existed!")

    # create file and write content
    filePath = newDirPath + "demo2.txt"
    if not os.path.exists(filePath):
        f = open(filePath, "x")
    else:
        f = open(filePath, "w")
        print(filePath, "has existed!")
    f.write("for testing purpose!")

    # read file
    f = open(filePath)
    print(f.read())
    f.close()

    isDel = input("are your sure to delete file : " + filePath + "[Y / N]?")
    if isDel == "Y" or isDel == "y":
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            print("quit delete!")
    else:
        print(filePath, "doesn't exist!")


    if not os.path.exists(newDirPath):
        os.path.

finally:
    f.close()
