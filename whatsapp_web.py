import pywhatkit as kit
from datetime import datetime, timedelta
import time
import random
#import gui

def send_e(data):
    for entry in data:
        phone = str(entry['number']).strip()
        messag = str(entry['message']).strip()
        time_str = str(entry['time']).strip()
    print(phone)
    try:
            time_str= datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
            time_str= datetime.strptime(time_str, "%H:%M")
    H=time_str.hour
    M=time_str.minute
    wait=random.randrange(1,25)
    phone="+"+ str(phone)
    try:
        if phone.value is not  None:
            gui.mas()
        kit.sendwhatmsg(phone,messag , H,M,60-wait,True,6)
        gui.start()
        M = M +2
        M=M %60
    except Exception as e:
        print(e)
        M = (M + 2)% 60
        if M < 2:
            H = (H + 1) % 24
        print("second time")
        kit.sendwhatmsg(phone,messag,H, M,70-wait,True,4)
print("adsdd")