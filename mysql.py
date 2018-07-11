#!/usr/bin/python3

import pymysql
import time
import sys,os

print("----HI!----")

#Catch data
co2 = 1500
light = 50
temp = 25
moisture = 60
#sql = "INSERT INTO `sensors`(sens_id, date_time, CO2) VALUES (NULL,"+str(int(time.time()))+","+str(int(score/count))+")"

sql = "INSERT INTO `data`(`id`, `co2`, `light`, `temp`, `moisture`, `time`) VALUES (NULL,"+str(co2)+","+str(light)+","+str(temp)+","+str(moisture)+","+str(int(time.time()))+")"
print(sql)
try:
    db = pymysql.connect("212.34.238.190","root","my_password","greenhouse" )
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
except:
    print('---ERROR: Server error, initial or upload---')
    try:
        db = pymysql.connect("212.34.238.190","root","my_password","iot" )
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
    except:
         print("AAAAAAAAAAAAAAAAAAAA!!!!! apocalips, I'm going, goodbye")
         os.execl(sys.executable, sys.executable, *sys.argv)
         sys.exit(0)
