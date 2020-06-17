# OANDA trading data streaming
from API import OANDA_api
import requests
import json
import ast

session = requests.Session()

APIKEY = OANDA_api
SYMBOLS = ['EUR_USD','USD_JPY','GBP_USD','AUD_USD','USD_CAD','USD_CNY','USD_CHF','USD_HKD']

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {APIKEY}',
}

response = requests.get('https://api-fxpractice.oanda.com/v3/accounts', headers=headers)

accountid = response.json()['accounts'][0]['id']


summary = requests.get(f'https://api-fxpractice.oanda.com/v3/accounts/{accountid}/summary', headers=headers)

## Use this to get the price history
# params = (
#     ('count', '30'),
#     ('price', 'M'),
#     ('granularity', 'M1'),
# )

# for symbol in SYMBOLS:
#     candle = requests.get(f'https://api-fxpractice.oanda.com/v3/instruments/{symbol}/candles', headers=headers, params=params)
#     for i in range(0,30):
#             print(candle.json()['candles'][i])


headers = {
    'Authorization': f'Bearer {APIKEY}',
}

params = (
    ('instruments', 'EUR_USD'), #USD_CAD,USD_JPY,GBP_USD,AUD_USD,USD_CNY,USD_CHF,USD_HKD'),
)


r = requests.get(f'https://stream-fxpractice.oanda.com/v3/accounts/{accountid}/pricing/stream', headers=headers, params=params, stream=True)

for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        print(decoded_line)  
        print(json.loads(decoded_line)['type'])