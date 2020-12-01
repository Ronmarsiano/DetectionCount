#! /usr/local/bin/python3
import subprocess
import os, os.path


def print_ok(input_str):
    print("\033[1;32;40m" + input_str + "\033[0m")


def print_error(input_str):
    print("\033[1;31;40m" + input_str + "\033[0m")


def pull_detectins():
    clone = subprocess.Popen(["git", "clone","https://github.com/Azure/Azure-Sentinel.git"], stdout=subprocess.PIPE)
    o, e = clone.communicate()
    if e is not None:
        print_error(str(e))


def fetch_git_repo():
    subprocess.Popen(["git", "clone","https://github.com/Azure/Azure-Sentinel.git"], stdout=subprocess.PIPE)


def delete_detection():
    delete_command = subprocess.Popen(["rm","-fr", "Azure-Sentinel"], stdout=subprocess.PIPE)
    o, e = delete_command.communicate()
    if e is not None:
        print_error(str(e))
    print_ok("Deleted")


def count_files(dir):
    counter = 0
    for name in os.listdir(dir):
        if os.path.isdir(dir + name + "/"):
            counter = counter + count_files(dir + name + "/")
        else:
            counter = counter + 1
    return counter


def main():
    pull_detectins()
    fetch_git_repo()
    print_ok(str(count_files("./Azure-Sentinel/Detections/")))
    delete_detection()


main()