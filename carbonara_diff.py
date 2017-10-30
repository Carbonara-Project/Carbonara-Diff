import json
import sys
import os
from collections import defaultdict

class Proc:
    def __init__(self, name, program, offset):
        self.name = name
        self.program = program
        self.offset = offset


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
    for path in os.listdir("./carbonara_diff_db"):
        #print path
        loadInfo(os.path.join("./carbonara_diff_db", path))


def strMatch(d):
    s = "["
    for e in xrange(8):
        if e in d.keys():
            s += d[e]
        else:
            s += " "
    s += "]"
    return s

def diff(path):
    fd = open(path)
    data = json.load(fd)
    fd.close()

    for d in data["procs"]:
        match = defaultdict(int)
        match_arr = defaultdict(dict)
        
        for p_id in hashes1[d["hash1"]]:
            match[p_id] += 1
            match_arr[p_id][0] = '*'
        for p_id in hashes2[d["hash2"]]:
            match[p_id] += 2
            match_arr[p_id][1] = '*'
        for p_id in hashes3[d["hash3"]]:
            match[p_id] += 3 * (len(d["raw"]) // 100 +1) #more significative with big functions
            match_arr[p_id][2] = '*'
        for p_id in hashes4[d["hash4"]]:
            match[p_id] += 5 * (len(d["raw"]) // 100 +1)
            match_arr[p_id][3] = '*'
        for p_id in hashes5[d["hash5"]]:
            match[p_id] += 10
            match_arr[p_id][4] = '*'
        for p_id in hashes6[d["hash6"]]:
            match[p_id] += 8
            match_arr[p_id][5] = '*'
        for p_id in hashes7[d["hash7"]]:
            match[p_id] += 10
            match_arr[p_id][6] = '*'
        for p_id in hashes8[d["full_hash"]]:
            match[p_id] += 100
            match_arr[p_id][7] = '*'
        
        sr = sorted(match, key=match.get)
        sr.reverse()
        print "[0x%x] %s" % (d["offset"], d["name"])
        i = 0
        for p_id in sr:
            if i >= 3:
                break
            print "        %s (%d) <%s :: 0x%x> %s" % (strMatch(match_arr[p_id]), match[p_id], procs[p_id].program, procs[p_id].offset, procs[p_id].name)
            i += 1
        print


def main():
    if len(sys.argv) < 2:
        print "usage: python carbonara_diff.py data.json\n"
        exit(1)
    loadDB()
    diff(sys.argv[1])
    #save to db
    fd = open(sys.argv[1])
    sv = open(os.path.join("./carbonara_diff_db", os.path.basename(sys.argv[1])), "w")
    sv.write(fd.read())
    sv.close()
    fd.close()
  
main()
   
