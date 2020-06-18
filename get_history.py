from API import OANDA_api
import requests
import json
import pandas as pd
import numpy as np

session = requests.Session()

APIKEY = OANDA_api
SYMBOLS = ['EUR_USD','USD_JPY','GBP_USD','AUD_USD','USD_CAD','USD_CNY','USD_CHF','USD_HKD']

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {APIKEY}',
}

response = requests.get('https://api-fxpractice.oanda.com/v3/accounts', headers=headers)

accountid = response.json()['accounts'][0]['id']






## Use this to get the price history
periods = 5000
params = (
    ('count', f'{periods}'),
    ('price', 'M'),
    ('granularity', 'M1'),
)

for symbol in SYMBOLS:
    candle = requests.get(f'https://api-fxpractice.oanda.com/v3/instruments/{symbol}/candles', headers=headers, params=params)
    hist = pd.DataFrame()
    for i in range(0,periods):
        # print(pd.DataFrame(candle.json()['candles'][i]))
            # hist[symbol+str(i)] = candle.json()['candles'][i]['mid']['c']
            # hist[symbol+'time'+str(i)] = candle.json()['candles'][i]['time']
        hist = hist.append(pd.DataFrame(candle.json()['candles'][i]), ignore_index=True)
    hist.to_json(f'{symbol}.json')


# with open("history.json", 'w') as f:
#     # indent=2 is not needed but makes the file 
#     # human-readable for more complicated data
#     json.dump(hist, f,) 





    # for i in range(0,periods):
    #         print(candle.json()['candles'][i])

