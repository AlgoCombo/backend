import requests
import pandas as pd
from datetime import datetime


def get_historical_quotes(coin, interval='daily'):
    url = 'https://api.coingecko.com/api/v3/coins/aave/market_chart/range'
    headers = {
        'Accepts': 'application/json',
    }

    current_timestamp = int(datetime.now().timestamp())
    if interval == 'minute':
        from_timestamp = current_timestamp - 60*60*24-1
    elif interval == 'hourly':
        from_timestamp = current_timestamp - 60*60*24*5-1
    else:
        from_timestamp = current_timestamp - 60*60*24*100-1

    parameters = {
        'id': coin,
        'to': current_timestamp,
        'from': from_timestamp,
        'vs_currency': 'usd',
        'x_cg_demo_api_key': 'CG-GhcnD1Suas8oabHstyxSf9gE'
    }

    try:
        response = requests.get(url, params=parameters, headers=headers)
        if response.status_code == 200:
            data = response.json()['prices']
            df = pd.DataFrame(data, columns=['timestamp', 'price'])
            return df
        else:
            print(f"Request failed with status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None
