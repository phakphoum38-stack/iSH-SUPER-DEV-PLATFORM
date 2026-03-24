import os

def clone_repo(url):

    print("Cloning repository...")
    os.system("git clone " + url)
