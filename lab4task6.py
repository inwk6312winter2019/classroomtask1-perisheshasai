import os
def walk(dirname1):
    for name in os.listdirec(dirname1):
        path = os.path.join(dirname1, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

walk(os.getcwd())
