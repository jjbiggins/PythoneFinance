#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : goog.py
# Author            : Joe Biggins <jjbiggins@joebiggins.io>
# Date              : 21.06.2020
# Last Modified Date: 21.06.2020

import sys
import os
import sys
import numpy as np
import pandas as pd

import pandas_datareader as pdr
import pandas_datareader.data as web


import matplotlib
import matplotlib.pyplot as plt

def readData():
    df = web.DataReader('GOOG', 'quandl', start='2009-03-14', end='2020-06-01', api_key='9UfDvyheeFPxTJxovpBz')
    print(df.tail())


def volatilityAnalytics():

    goog = web.DataReader('GOOG', 'quandl', start='2009-03-14', end='2020-06-01', api_key='9UfDvyheeFPxTJxovpBz')
    goog['Log_Ret'] = (np.log(goog['Close'] / goog['Close'].shift(1)))
    goog['Volatility'] = goog['Log_Ret'].rolling( window=252).std() * np.sqrt(252)
    print(goog['Volatility'])

    goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8,6))
    plt.show()

if __name__ == "__main__":
    #readData()
    volatilityAnalytics()
