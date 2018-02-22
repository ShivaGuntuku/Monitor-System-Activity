#!/usr/bin/python3

import pyautogui as py
from time import sleep
from power_off import shutOff, power_flag, activity
# from firebase import firebase


monitor = list()
count = 0 
while True:
    # firebase = firebase.FirebaseApplication(
    #     'https://remotedrive-v3.firebaseio.com/', 
    #     None)
    monitor.append(py.position())
    sleep(60)
    count+=1

    if count == power_flag('strict') :
        activity = activity(monitor,count)
        if activity is not None:
            print "success...."
            break

print monitor




