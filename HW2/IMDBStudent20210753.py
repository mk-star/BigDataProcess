#!/usr/bin/python3
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as fr:
    genre = dict()
    while True:
        row = fr.readline()
        if not row:
            break
        
        data = row.split("::")
        datalist = data[2].split("|")
        
        genres = []
        for d in datalist:
            genres.append(d.rstrip("\n"))
        
        for g in genres:
            if g not in genre:
                genre[g] = 1
            else:
                genre[g] += 1

with open(file2, "w") as fw:
    for g in genre:
        fw.write("%s %d\n" % (g, genre[g]))
