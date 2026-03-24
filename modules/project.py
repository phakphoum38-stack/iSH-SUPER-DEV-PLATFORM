import os

def create_project(name):

    base = "projects"

    if not os.path.exists(base):
        os.mkdir(base)

    path = base + "/" + name

    if os.path.exists(path):
        print("Project exists")
        return

    os.mkdir(path)

    with open(path + "/main.py", "w") as f:
        f.write("print('New project created')")

    print("Project created:", name)
