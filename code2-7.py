#-*- coding: UTF-8 -*- 
import time

currentTime = time.time()

# get total seconds from 1970. 1. 1. 00:00:00
totalSeconds = int(currentTime);

# get current seconds
currentSecond = totalSeconds % 60

# calculate total minutes
totalMinutes = totalSeconds // 60

# calculate current minute
currentMinute = totalMinutes % 60

# calculate total hours
totalHours = totalMinutes // 60

# get the hour part of current time
currentHour = totalHours % 24;

# show the result [0.xx]
print("current clock: ", currentHour, ":", currentMinute,":", currentSecond)
