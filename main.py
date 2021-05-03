# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Copyright 2021 zhangt2333. All Rights Reserved.
# Author-Github: github.com/zhangt2333

import os
import re
import sys

import requests

username = os.environ["USERNAME"]
hw_index = int(re.findall(r'homework([0-9]+)', os.environ["ISSUE_TITLE"])[0])

def hw1():
    response = requests.get('https://raw.githubusercontent.com/{}/hw-gitStash/bugfix/1plus1.txt'.format(username))
    sys.exit(0 if '1+1=2' in response.text.strip().replace(' ', '') else -1)

def hw2():
    feature1 = requests.get('https://raw.githubusercontent.com/{}/hw-gitStash/feature1/feature1.txt'.format(username)).text.strip().replace(' ', '')
    feature1_2 = requests.get('https://raw.githubusercontent.com/{}/hw-gitStash/feature1/feature1_2.txt'.format(username)).text.strip().replace(' ', '')
    sys.exit(0 if '1+2=3' in feature1
                  and '1+3=4' in feature1
                  and '2+2=4' in feature1_2
                  and '2+3=5' in feature1_2
                  and '2+4=6' in feature1_2
                  and '2+5=7' in feature1_2
                  and '2+6=8' in feature1_2
             else -1)

methods = [hw1, hw2]
if __name__ == '__main__':
    methods[hw_index - 1]()