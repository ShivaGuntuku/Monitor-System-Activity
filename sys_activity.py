#!/usr/bin/python3

import pyautogui as py
from time import sleep
from power_off import shutOff, power_flag, activity
from firebase import firebase
from datetime import datetime


monitor = list()
firebase = firebase.FirebaseApplication(
    'https://remote-drive-9967e.firebaseio.com/', None)
count = 0 
while True:
    monitor.append(py.position())
    sleep(60)
    count+=1

    if count == power_flag('strict') :
        activity = activity(monitor,count)
        if activity is not None:
            now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            firebase.put('/Activity',now,"In Active")
            break

print monitor




