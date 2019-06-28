#!/usr/bin/python
#Developed by THYemre

import requests
from lxml import html

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

base_url = "https://www.hackthebox.eu/home/users/profile/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Cookie": "" # ADD YOUR COOKIES HERE FOR AUTH 
   "Cache-Control": "max-age=0"
}

r = requests.session()
getting = r.get(base_url,headers=headers)
print bcolors.OKBLUE + "DEVELOPED BY THYEMRE" + bcolors.ENDC
for i in range(36000,40000):
    print base_url + str(i)
    user_link = base_url + str(i)
    check_id = r.get(user_link)
    get_user = r.get(user_link,headers=headers)
    user_response = html.fromstring(get_user.content)
    check_datas = user_response.xpath('//h2[@class="no-margins"]/text()')
    user_owns = int(''.join(str(e) for e in check_datas[5].split()))
    if user_owns == 0:
        user_owns = 1
    member_date = int(''.join(str(e) for e in check_datas[7].split()))
    # MAIN CHECKING PART
    math = (member_date/user_owns)
    if math < 6:
        print bcolors.FAIL + "[- POSSIBLE CHEATER DETECTED -] " + base_url + str(i) + bcolors.ENDC
    else:
        print bcolors.OKGREEN + "[+ USER IS OK +]" + base_url + str(i) + bcolors.ENDC
