import requests

def scrape():
    resp = requests.get(url+coin) #gets the url of the json file with all the information
    resp_json = resp.json() # translates json file
    return float(resp_json[0]['price_usd']) # gets value "price_usd" from json file

url = 'https://api.coinmarketcap.com/v1/ticker/' #api url
coin = 'bitcoin' #coin name
last_price = None # the latest set price

while True:
    last_price = scrape() # gets the information from the scrape function
    if last_price != last_price: # if the value is not the same
        print("Latest Price: ", last_price, "USD") # prints price
        last_price = last_price # sets new value to last_price