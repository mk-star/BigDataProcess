#!/usr/bin/python3

import calendar
with open("uber.dat", "r") as fr:
    dayofweek = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    while True:
        row = fr.readline()
        if not row:
            break

        data = row.split(",")
        date = data[1].split("/")
        day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
        with open("uberoutput.txt", "at") as fw:
            fw.write("%s,%s %s,%s" % (data[0], dayofweek[day], data[2], data[3]))
