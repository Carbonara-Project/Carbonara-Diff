import json
import sys
import os
from collections import defaultdict

class Proc:
    def __init__(self, name, program, offset):
        self.name = name
        self.program = program
        self.offset = offset
    def __str__():
        return "[%s : %x] :: 
procs = []

hashes1 = defaultdict(list)
hashes2 = defaultdict(list)
hashes3 = defaultdict(list)
hashes4 = defaultdict(list)
hashes5 = defaultdict(list)
hashes6 = defaultdict(list)
hashes7 = defaultdict(list)
hashes8 = defaultdict(list)


def loadInfo(path):
    fd = open(path)
    data = json.load(fd)
    fd.close()
    
    for d in data["procs"]:
        proc_id = len(procs)
        procs.append(Proc(d["name"], data["program"]["filename"], d["offset"]))
        
        hashes1[d["hash1"]].append(proc_id)
        hashes2[d["hash2"]].append(proc_id)
        hashes3[d["hash3"]].append(proc_id)
        hashes4[d["hash4"]].append(proc_id)
        hashes5[d["hash5"]].append(proc_id)
        hashes6[d["hash6"]].append(proc_id)
        hashes7[d["hash7"]].append(proc_id)
        hashes8[d["full_hash"]].append(proc_id)


def loadDB():
    for path in os.listdir("./carbonara_diff_db")
        loadInfo(path)


def diff(path):
    fd = open(path)
    data = json.load(fd)
    fd.close()

    for proc in data["procs"]:
        
        match = {}
        if proc["hash1"] in hashes1:
            for i in xrange(len(names)):
                if hashes1[i] == proc["hash1"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(1)
        if proc["hash2"] in hashes2:
            for i in xrange(len(names)):
                if hashes2[i] == proc["hash2"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(2)
        if proc["hash3"] in hashes3:
            for i in xrange(len(names)):
                if hashes3[i] == proc["hash3"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(3)
        if proc["hash4"] in hashes2:
            for i in xrange(len(names)):
                if hashes2[i] == proc["hash4"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(4)
        if proc["hash5"] in hashes5:
            for i in xrange(len(names)):
                if hashes5[i] == proc["hash5"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(5)
        if proc["hash6"] in hashes6:
            for i in xrange(len(names)):
                if hashes6[i] == proc["hash6"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(6)
        if proc["hash7"] in hashes7:
            for i in xrange(len(names)):
                if hashes7[i] == proc["hash7"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(7)
        if proc["full_hash"] in hashes8:
            for i in xrange(len(names)):
                if hashes8[i] == proc["full_hash"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(8)
        










def main():
    if len(sys.argv) < 3:
        print "usage: python carbonara_diff.py data1.json data2.json\n"
        exit(1)
    file1 = open(sys.argv[1])
    file2 = open(sys.argv[2])
    data1 = json.load(file1)
    data2 = json.load(file2)
    file1.close()
    file2.close()
    
    file1 = open(program)
    data1 = json.load(file1)
    file1.close()
    i = 0
    for proc in data1["procs"]:
        names.append(proc["name"])
        #names_dict[i] = proc["name"]
        hashes1.append(proc["hash1"])
        hashes2.append(proc["hash2"])
        hashes3.append(proc["hash3"])
        hashes4.append(proc["hash4"])
        hashes5.append(proc["hash5"])
        hashes6.append(proc["hash6"])
        hashes7.append(proc["hash7"])
        hashes8.append(proc["full_hash"])
        i += 1
    
    for proc in data2["procs"]:
        
        match = {}
        if proc["hash1"] in hashes1:
            for i in xrange(len(names)):
                if hashes1[i] == proc["hash1"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(1)
        if proc["hash2"] in hashes2:
            for i in xrange(len(names)):
                if hashes2[i] == proc["hash2"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(2)
        if proc["hash3"] in hashes3:
            for i in xrange(len(names)):
                if hashes3[i] == proc["hash3"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(3)
        if proc["hash4"] in hashes2:
            for i in xrange(len(names)):
                if hashes2[i] == proc["hash4"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(4)
        if proc["hash5"] in hashes5:
            for i in xrange(len(names)):
                if hashes5[i] == proc["hash5"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(5)
        if proc["hash6"] in hashes6:
            for i in xrange(len(names)):
                if hashes6[i] == proc["hash6"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(6)
        if proc["hash7"] in hashes7:
            for i in xrange(len(names)):
                if hashes7[i] == proc["hash7"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(7)
        if proc["full_hash"] in hashes8:
            for i in xrange(len(names)):
                if hashes8[i] == proc["full_hash"]:
                    n = names[i]
                    match[n] = match.get(n, [])
                    match[n].append(8)
                    #print proc["name"] + "  " + n
                    
        print "[[[ %s ]]]" % proc["name"]
        mx = 0
        nm = "NOT MATCH"
        ma = {}
        for m in match:
            ma[m] = len(match[m])
        a = sorted(ma, key=ma.get)

        if len(a) > 0:
            for m in ma:
                if m == a[-1]:
                    print "         %d :: %s" % (ma[m], m)
        if len(a) > 1:
            for m in ma:
                if m == a[-2]:
                    print "         %d :: %s" % (ma[m], m)
        if len(a) > 2:
            for m in ma:
                if m == a[-3]:
                    print "         %d :: %s" % (ma[m], m)
        print
        
main()
   
