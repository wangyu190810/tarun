import os
import sys

def main():
    print sys.argv
    if len(sys.argv) > 1:
       filename = sys.argv[1]

       os.system("tar -xvf %s" %filename)

