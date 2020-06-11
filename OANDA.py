# OANDA trading data streaming
from API import OANDA_api
import requests


APIKEY = OANDA_api
SYMBOLS = ['EUR_USD']

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {APIKEY}',
}

response = requests.get('https://api-fxpractice.oanda.com/v3/accounts', headers=headers)
print(response.headers)
print(response.json())

accountid = response.json()['accounts'][0]['id']
print(accountid)


summary = requests.get(f'https://api-fxpractice.oanda.com/v3/accounts/{accountid}/summary', headers=headers)

print(summary.json())


instruments = requests.get(f'https://api-fxpractice.oanda.com/v3/accounts/{accountid}/instruments', headers=headers)

print(instruments.json()['instruments'][0]['name'])

params = (
    ('count', '30'),
    ('price', 'M'),
    ('granularity', 'M1'),
)

candle = requests.get(f'https://api-fxpractice.oanda.com/v3/instruments/{SYMBOLS[0]}/candles', headers=headers, params=params)

print(candle.json()['candles'])