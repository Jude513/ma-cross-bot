#!/usr/bin/env python

import yfinance as yf
from datetime import datetime as dt
import pytz
import time

def getData(ticker_, period_, interval_):
    while True:
        data = yf.download(ticker_, period=period_, interval=interval_, threads=True)
        print(f"{data['Close'].tail(1)}\n@{dt.now().strftime('%H:%M:%S')}")
        time.sleep(60)

getData('AAPL', '1d', '1m')
