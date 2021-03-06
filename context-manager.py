class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)
    def __enter__(self):
        print("enter")
        return self.file
    def __exit__(self, type, value, traceback):
        print (f"{type}: {value} {traceback} ")
        print("exit")
        self.file.close()

# with File("file.txt", "w") as f:
#     print("run")
#     f.write("xin chao")
#     #raise Exception()

## using lib
from contextlib import contextmanager

@contextmanager
def file(filename, method):
    file = open(filename, method)
    yield file
    file.close()

with file("file.txt", "w") as f:
    print("run")
    f.write("xin chao contextlib")
    #raise Exception()