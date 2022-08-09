#!/usr/bin/python3
"""Alta3 Research - tracking ISS updated output"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """runtime code"""
    groundctrl = requests.get(MAJORTON)

    helmet = groundctrl.json()

    print('People in space: ' + str(helmetson['number']))

    for x in people:
        print(x['name'], "is on the" + x['craft'])

if __name__ == "__main__":

