import playsound
import datetime
import time

print("Enter the Alarm Details:")
h = int(input("Enter the hour: "))
m = int(input("Enter the minute: "))
s = int(input("Enter the seconds: "))

alarm_str = "{:02d}-{:02d}-{:02d}".format(h, m, s)  

while True:
    current_time = datetime.datetime.now().time()
    current_time_str = current_time.strftime("%H-%M-%S")

    if current_time_str == alarm_str:
        playsound.playsound("a.mp3")
        print("Alarm triggered")
        break

    time.sleep(1)
