#!/usr/bin/python3

import requests


## function that gets the random quote
def get_random_quote():
	try:
		## fetch data from the api
		response = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
		if response.status_code == 200:
			## extracting the core data
			data = response.json()
			## getting the quote from the data
			print(data[0]['quote'])
		else:
			print("Error while getting quote")
	except Exception as err:
		print("Something went wrong! Try Again!", err)

get_random_quote()

if __name__ == "__get_random_quote__":
   get_random_quotes()
