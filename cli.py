from modules.shell import run_shell
from modules.github import clone_repo
from modules.project import create_project
from modules.system import system_info
from modules.package import install_package
from modules.ai import ai_help

def start_cli():

    while True:

        cmd = input("SUPERDEV> ")

        if cmd == "exit":
            break

        elif cmd.startswith("run "):
            run_shell(cmd[4:])

        elif cmd.startswith("clone "):
            clone_repo(cmd[6:])

        elif cmd.startswith("create "):
            create_project(cmd[7:])

        elif cmd.startswith("install "):
            install_package(cmd[8:])

        elif cmd == "system":
            system_info()

        elif cmd.startswith("ai "):
            ai_help(cmd[3:])

        else:
            print("Unknown command")
