#!/usr/bin/python3

import calendar
with open("uber.dat", "r") as fr:
    dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    result = dict()
    while True:
        row = fr.readline()
        if not row:
            break

        data = row.split(",")
        date = data[1].split("/")
        day = dayofweek[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))]

        if day not in result:
            result[day] = []
        else:
            result[day].append((data[0], data[2], data[3]))
for day in dayofweek:
    result[day].sort(key=lambda x: x[0])

with open("uberoutput.txt", "wt") as fw:
    for day in dayofweek:
        for r in result[day]:
            fw.write("%s,%s %s,%s" % (r[0], day, r[1], r[2]))
