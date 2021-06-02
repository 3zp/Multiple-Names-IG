import requests
import os
from os import system
from uuid import uuid4
import json
system("title " + "Multiple Names")
req = requests.session()
uid = uuid4()
username = ''
password = ''
name = ''
print("""       
Multiple 
Name
        """)
username = input("Username : ")
password = input("Password : ")
name = '''
😤
😤
😤
😤
😤
😤
😤
😤
😤
'''

logurl = 'https://i.instagram.com/api/v1/accounts/login/'

 
headers = {
    'User-Agent': 'Instagram 113.0.0.39.121 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US",
    "X-IG-Capabilities": "3brTvw==",
    "X-IG-Connection-Type": "WIFI",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'Host': 'i.instagram.com',
    'Connection': 'keep-alive'
}
url = 'https://i.instagram.com/api/v1/accounts/set_phone_and_name/'
data = {
 
    "first_name": name
}
def c():
    global coo
    r2 = req.post(url, headers=headers, data=data, cookies=coo).status_code
    if r2 == 200:
      print(f"Changed name to :\n",name)
      input()
    else:
        print(f"Error")
        input()
        exit()
logdata = {
    'uuid': uid,
    'password': password,
    'username': username,
    'device_id': uid,
    'from_reg': 'false',
    '_csrftoken': 'missing',
    'login_attempt_countn': '0'
}

 
def login():
    global log, loginJS
    global coo
    log = req.post(logurl, headers=headers, data=logdata)
    loginJS = log.json()
    if 'logged_in_user' in log.text:
        print("Logged into",username)
        coo = log.cookies
        c()
        pass
    else:
        print("Error")
        exit()
login()
