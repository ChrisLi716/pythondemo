x = "hello"
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else:
    print("success")
finally:
    print("end.")


def write2file(file: str):
    try:
        f = open(file)
        f.write("Lorum Ipsum")
    except UnboundLocalError:
        print("Something went wrong when writing to the file")
    finally:
        f.close()


write2file("C:/Users/Dell/Desktop/demo.txt")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
