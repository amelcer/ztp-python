from connection import Database
from datetime import datetime
from time import sleep
import random


DBNAME = "metrics"
# TODO Device {id} form argument / config file
DEVICE_ID = 1

# TODO Intervals from database
MEASUREMENT_TIME = 1
INSERT_TIME = 5

db = Database(db=DBNAME, password='admin')

temp = 20
humi = 50
volts = 4
n = int(INSERT_TIME / MEASUREMENT_TIME)
i = 0
sql = f"INSERT INTO data VALUES"


while (True):
    strtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql += f"(NULL, {DEVICE_ID}, '{strtime}', {temp}, {humi}, {volts}),"
    i += 1
    if i >= n:
        i = 0
        sql = sql.rstrip(",") + ";"
        print(sql)
        db.exec(sql)
        sql = f"INSERT INTO data VALUES"
    temp += random.uniform(-0.5, 0.5)
    humi += random.uniform(-1.0, 1.0)
    volts += random.uniform(-0.01, 0)
    sleep(MEASUREMENT_TIME)
