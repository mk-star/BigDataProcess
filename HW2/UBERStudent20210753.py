#!/usr/bin/python3

import calendar
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, "r") as fr:
    dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    result = dict()
    while True:
        row = fr.readline()
        if not row:
            break

        data = row.split(",")
        date = data[1].split("/")
        day = dayofweek[calendar.weekday(int(date[2]), int(date[0]), int(date[1]))]

        if (data[0], day) not in result:
            result[(data[0], day)] = [int(data[2]), int(data[3])]
        else:
            result[(data[0], day)][0] += int(data[2])
            result[(data[0], day)][1] += int(data[3])

with open(file2, "w") as fw:
    for key, values in result.items():
        fw.write("%s,%s %s,%s\n" % (key[0], key[1], values[0], values[1]))
