import os
import sys


def main():
    print(sys.argv)
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        extract(filename)
    else:
        print("tarun file_name")

def extract(filename):
    name = filename.split(".")
    if "tar" in name and len(name) == 1:
        os.system("tar -xvf %s" %filename)
    elif ("tar" in name and "gz" in name) or "tgz" in name:
        os.system("tar -zxvf %s" %filename)
    elif "gz" in name:
        os.system("gunzip %s" %filename)
    elif "bz2" in name:
        os.system("bzip2 -d %s" %filename)
    elif "bz" in name:
        os.system("bunzip2 -d %s" %filename)
    elif "tar" in name and "bz" in name:
        os.system("tar jxvf %s" %filename)
    elif ("Z" or "z") in name:
        os.system("uncompress %s" %filename)
    elif ("tar" and "Z" in name ) or ("tar" and "z" in name):
        os.system("tar Zxvf %s" %filename)
    elif "zip" in name:
        os.system("unzip %s" %filename)


