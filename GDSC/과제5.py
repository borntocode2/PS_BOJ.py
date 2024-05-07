import datetime 
import time

while 1:
    current = datetime.datetime.now()
    print("지금은 {}시{}분{}초입니다.".format(current.hour,current.minute,current.second))
    time.sleep(1)
