# from bitcoinaddress import Wallet  #bitcoinaddress is a module and Wallet is class imported from module
# wallet = Wallet() #created the obj
# print(wallet)


# import requests
# from bs4 import BeautifulSoup as bs
# URL = 'https://coinmarketcap.com/currencies/bitcoin/'
# req = requests.get(URL)

# soup = bs(req.content,'html.parser')

# price = soup.find('div', {'class':'priceValue'})
# extract = price.select_one('span')

# print(f"Bitcone price today is {extract.text} per (BTCm/USD)")

import requests
from bs4 import BeautifulSoup as bs

# Step 1: Set a User-Agent header so the website knows we are a real web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

URL = 'https://coinmarketcap.com/currencies/bitcoin/'
req = requests.get(URL, headers=headers)

soup = bs(req.content, 'html.parser')

# Step 2: Find the span element directly using its new HTML attribute
# CoinMarketCap uses data-test="text-cdp-price-display" for the main price
price_span = soup.find('span', {'data-test': 'text-cdp-price-display'})

# Step 3: Safely check if we found the price before reading its text!
if price_span is not None:
    print(f"Bitcoin price today is {price_span.text} per (BTC/USD)")
else:
    print("Could not find the price element on the page. The website structure may have changed!")


