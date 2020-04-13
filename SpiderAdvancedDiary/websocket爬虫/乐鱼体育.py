# -*- encoding: utf-8 -*-
#Time : 2020/04/13 11:48:48
import requests
import json
import websocket
import time
import math

def getToken():
    r = requests.get('https://live.611.com/Live/GetToken')
    return json.loads(r.text)['Data']

def getMessage():
    message1 = {
        "command": "RegisterInfo",
        "action": "Web",
        "ids": [],
        "UserInfo": {
            "Version": str([int(time.time()*1000)]) + '{"chrome":true,"version":"80.0.3987.149","webkit":true}',
            "Url": "https://live.611.com/zq"
        }
    }
    message2 = {
        "command": "JoinGroup",
        "action": "SoccerLiveOdd",
        "ids": []
    }
    message3 = {
	    "command": "JoinGroup",
	    "action": "SoccerLive",
	    "ids": []
    }
    return json.dumps(message1),json.dumps(message2),json.dumps(message3)

def sendMessage(m1,m2,m3):
    ws = websocket.create_connection(url)
    ws.send(m1)
    ws.send(m2)
    ws.send(m3)
    while True:
        content = ws.recv()
        print(content)
    

if __name__ == "__main__":
    token = getToken()
    url = 'wss://push.611.com:6119/' + token
    m1,m2,m3 = getMessage()
    sendMessage(m1,m2,m3)