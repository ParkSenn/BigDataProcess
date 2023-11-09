#!/usr/bin/python3
import calendar
import sys

fileName = sys.argv[1]

output = []
weekDay = "MON/TUE/WED/THU/FRI/SAT/SUN"
weekDay_list = weekDay.split("/")

with open(fileName, "rt") as fp:
    for line in fp:
        info = line.split(",") # 지역, 날짜, 차량 수, 여행
        baseNum = info[0]
        date = info[1]
        vehicles = info[2]
        trips = info[3]
        str_dt_list = date.split("/") 
        date_list = [int(i) for i in str_dt_list] # month, day, year
        day = calendar.weekday(date_list[2], date_list[0], date_list[1])
        wd = weekDay_list[day] # 구한 요일
        result = f"{baseNum},{wd} {vehicles},{trips}"
        output.append(result)


outputName = sys.argv[2]
with open(outputName, "w") as f:
    f.writelines(output)