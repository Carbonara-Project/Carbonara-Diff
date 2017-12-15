import os
import sys

yet = os.listdir("./carbonara_diff_db")

for path in os.listdir(sys.argv[1]):
    if path not in yet:
        print ">>>", path
        os.system("cd " + sys.argv[1] + "; python -m carbonara_cli " + path)
