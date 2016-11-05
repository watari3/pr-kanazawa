'''
F3:3B:15:7E:29:BB.e9484eb5107adfef1af6a0dc65c03232.localhost.deviceconnect.org
Host.e87e3213b730843a437ff6c676899df0.localhost.deviceconnect.org
'''

import requests
import time
import os

while True:
    # deviceのIP変更
    hoge = requests.get('http://172.16.42.147:4035/gotapi/health/heartrate?serviceId=F3%3A3B%3A15%3A7E%3A29%3ABB.e9484eb5107adfef1af6a0dc65c03232.localhost.deviceconnect.org&accessToken=null').json()
    heartRate = hoge['heartRate']
    if heartRate > 100:
        heartRate = 100
    elif heartRate < 70:
        heartRate = 70
    os.system('python mabeee.py devices/1/set?pwm_duty=' + str(heartRate))
    #ファイルチェックで　止めたり　できないか　break
    time.sleep(1)
