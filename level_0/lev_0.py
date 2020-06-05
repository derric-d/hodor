#!/usr/bin/python3
"""
hodor level 0
Send 1024 votes to my school id with post request to url
"""
import requests


datadic = {'id': '1345', 'holdthedoor': 'submit'}
target_url = "http://158.69.76.135/level0.php"
num_votes = 1024
reqs_made = 0
fails = 0


print("start @ {}".format(reqs_made))
while reqs_made < num_votes and fails < 100:
    try:
        res = requests.post(target_url, data=datadic)
        fails = 0
        reqs_made += 1
        print("req {} passed".format(reqs_made))
    except Exception as e:
        print(e)
        fails += 1

print("end w/ {} votes passed from 1024".format(reqs_made))
