import json
import sys
import os
from datasketch import *
from collections import defaultdict

class Proc:
    def __init__(self, name, program, offset):
        self.name = name
        self.program = program
        self.offset = offset


procs = []

vexhash = {}
flowhash = {}
#fullhash = defaultdict(list)


forest = MinHashLSHForest(num_perm=64)
forest_flow = MinHashLSHForest(num_perm=32)


def loadInfo(path):
    fd = open(path)
    data = json.load(fd)
    fd.close()
    
    for d in data["procs"]:
        off = d["offset"]
        d = d["proc_desc"]
        proc_id = len(procs)
        
        procs.append(Proc(d["name"], data["info"]["filename"], off))
        
        mal = data["program"]["md5"]
        
        #fullhash[d["full_hash"]].append(proc_id)
        
        
        lh = LeanMinHash.deserialize(d["vex_hash"].decode("hex"))
        vexhash[proc_id] = lh
        
        lhf = LeanMinHash.deserialize(d["flow_hash"].decode("hex"))
        flowhash[proc_id] = lhf
        
        forest.add(proc_id, lh)
        forest_flow.add(proc_id, lhf)
        


def loadDB():
    print "LOADING FILES FROM DISK..."
    #print os.listdir("./carbonara_diff_db")
    dirc = os.listdir("./carbonara_diff_db")
    for i in xrange(len(dirc)):
        if dirc[i].endswith(".json"):
            #print dirc[i]
            loadInfo(os.path.join("./carbonara_diff_db", dirc[i]))
            sys.stdout.write("\r %d / %d" % (i, len(dirc)))
            sys.stdout.flush()
    print


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
    
    forest.index()
    forest_flow.index()
    
    print "DIFF STARTED"
    
    import time
    start = time.time()
    
    mal = data["program"]["md5"]
    output = ""
    
    for d in data["procs"]:
        off = d["offset"]
        d = d["proc_desc"]
        
        #if "Exec" not in d["name"]:
        #    continue
        
        proc_id = len(procs)
        
        ll = len(d["raw"])
        
        procs.append(Proc(d["name"], data["info"]["filename"], off))
        
        lh = LeanMinHash.deserialize(d["vex_hash"].decode("hex"))
        lhf = LeanMinHash.deserialize(d["flow_hash"].decode("hex"))

        
        try:
            result = forest.query(lh, 12)
            fls = forest_flow.query(lhf, 12)
            
            match = defaultdict(int)
            
            cc = {}
            for r in result:
                j = lh.jaccard(vexhash[r])
                cc[r] = j
                match[r] += j * 100
            
            pp = {}
            for f in fls:
                j = lhf.jaccard(flowhash[f])
                pp[f] = j
                #match[f] += j * (ll / 1000)
                match[f] += (j ** 2) * (ll / 1000)
            
            output +=  "---- %s (%d bytes)----\n" % (d["name"], len(d["raw"]))
            
            sk = sorted(match, key=match.get, reverse=True)[:3]
            for k in sk:
                cj = match[k]
                on = "   <" + procs[k].program +"> "+ procs[k].name
                output += on + (100 - len(on))* " " + "   (" + str(int(cj)) + ")"
                if k in cc:
                    output += "\tVEX:" + str(cc[k])
                if k in pp:
                    output  += "\tFLOW:" + str(pp[k]) + ","+str((pp[k] ** 2) * (ll / 1000))
                output += "\n"
            output += "\n"
            
        except ValueError as ee:
            print "ERR", ee
            continue
            
    el = (time.time() - start)

    print output
    print "elapsed %d" % el

def main():
    if len(sys.argv) < 2:
        print "usage: python carbonara_diff.py data.json\n"
        exit(1)
    loadDB()
    diff(sys.argv[1])

  
main()
   
