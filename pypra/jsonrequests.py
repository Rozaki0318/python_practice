#! /usr/bin/env python3

import os
import requests
import json


path = '/data/feedback/'
filelist = [path + s for s in os.listdir(path)]
print(filelist)

for file in filelist:
    with open(file) as f:
        l = [s.strip() for s in f.readlines()]
        #print(l)
        dict_l = {"title": l[0], "name": l[1], "date": l[2], "feedback": l[3]}
        #print(dict_l)
        senddata = json.dumps(dict_l)
        print(senddata)
        res = requests.post('http://34.173.252.190/feedback', json=senddata, headers={'Content-Type': 'application/json'})
        print(res.status_code)