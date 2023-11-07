#!/usr/bin/python3

with open("movie.dat", "r") as fr:
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

with open("movieoutput.txt", "wt") as fw:
    for g in genre:
        fw.write("%s %d\n" % (g, genre[g]))