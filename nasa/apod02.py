#!/usr/bin/python3

import requests

#Import required libraries:

from datetime import datetime
import urllib.request
import smtplib 

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# Get today's date in YYYY-MM-DD format:

d = datetime.today().strftime('%Y-%m-%d')

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    # you don't want to put api keys directly into scripts
    # that way anyone who can see you script can see your key, which is a security risk
    # plus, you should already be reading in that key from your nasa.creds file
    # so you were adding it in twice :)
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()

