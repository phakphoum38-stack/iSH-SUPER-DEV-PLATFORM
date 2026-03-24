import os

def install_package(name):

    print("Installing:", name)

    os.system("apk add " + name)
