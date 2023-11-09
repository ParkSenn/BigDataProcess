#!/usr/bin/python3
import calendar
import sys

fileName = sys.argv[1]

output = dict()
weekDay = "MON/TUE/WED/THU/FRI/SAT/SUN"
weekDay_list = weekDay.split("/")

with open(fileName, "rt") as fp:
    for line in fp:
        info = line.split(",") # 지역, 날짜, 차량 수, 여행
        baseNum = info[0]
        date = info[1]
        vehicles = int(info[2])
        trips = int(info[3])       
        str_dt_list = date.split("/") 
        date_list = [int(i) for i in str_dt_list] # month, day, year
        day = calendar.weekday(date_list[2], date_list[0], date_list[1])
        wd = weekDay_list[day] # 구한 요일

        key = (baseNum, wd)
        if key not in output :
            output[key] = {"baseNum" : baseNum, "wd" : wd, 
                           "vehicles" : vehicles, "trips" : trips}
        else :
            output[key]['vehicles'] += vehicles
            output[key]['trips'] += trips


outputName = sys.argv[2]
with open(outputName, "w") as f:
    for key in output:
        sample = output[key]
        f.write("%s,%s %d,%d\n" % (sample["baseNum"], sample["wd"], sample["vehicles"], sample["trips"]))