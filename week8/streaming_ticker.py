import os
import operator as op
import numpy as np
import pandas as pd
import requests
import hvplot.pandas
import hvplot.streamz
from streamz.dataframe import PeriodicDataFrame

def main():
    # Load API key (read this in from a config.py file or type it in)
    if os.path.exists('config.py'):
        print('Reading in API key from config file')
        import config
        key = config.api_key
    else:
        key = input('Please enter your API key:')
    stock = 'GOOG'

    # Set up streaming dataframe
    df = PeriodicDataFrame(streaming_quotes, key=key, stock='GOOG', interval='5s')

    # Visualize data
    bidplot = df[['bidPrice']].hvplot.line(title='bidPrice', backlog=1000)
    askplot = df[['askPrice']].hvplot.line(title='askPrice', backlog=1000)
    hvplot.show(bidplot + askplot)


def make_request(key,stock):
    '''Function to make the API request'''
    # Set endpoint
    endpoint = f'https://api.tdameritrade.com/v1/marketdata/{stock}/quotes'
    # Define API payload
    payload = {
        'apikey': key,
    }
    # Make API request
    response = requests.get(url = endpoint, params=payload)
    # Parse as JSON
    data = response.json()
    results = []
    results.append(data[stock])
    # Convert to dataframe
    prices = pd.DataFrame(results)
    prices = prices[['bidPrice','askPrice']]
    return prices

def streaming_quotes(**kwargs):
    '''Callback function to get quotes'''
    key = kwargs.get('key')
    stock = kwargs.get('stock')
    df = make_request(key,stock)
    df['time'] = [pd.Timestamp.now(tz='US/Eastern')]

    return df.set_index('time')

if __name__ == "__main__":
    main()

