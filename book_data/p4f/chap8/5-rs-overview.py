# Rolling Statitics

 #Rolling statistics or financial indicators or financial studies are basic tools for financial chartlists and technical traders, for example. This section works with a single fianncial time series only:


import pandas as pd
import numpy as np


filename = '../source/tr_eikon_eod_data.csv'
data = pd.read_csv(filename, index_col=0, parse_dates=True)

# gets the data for Apple stock

sym = 'AAPL.O'
data = pd.DataFrame(data[sym]).dropna()


# It's straightforward to derive standared rolling statistics with pandas:

# Defines the window; I.e., the nummber of index values to include
window = 20

# Calculates the rolling minimum value
data['min'] = data[sym].rolling(window=window).min()

# Claculates the mean value
data['mean'] = data[sym].rolling(window=window).mean()

# Calculates the rolling standared deveation
data['std'] = data[sym].rolling(window=window).std()

# Calculates the rolling median value
data['median'] = data[sym].rolling(window=window).median()

# Calculates the rolling maximum value
data['max'] = data[sym].rolling(window=window).max()

# Calculates the exponentially weighted moving average, with decay in terms of a half life of 0.5
data['min'] = data[sym].ewm(halflife=0.5, min_periods=window).mean()


# plots the rolling statistics for the final 200 data rows
ax = data[['min', 'max']].iloc[-200:].plot(figsize=(10, 6), style=['g--', 'r--', 'g--'], lw=0.8)

# Adds the original time series data to the plot
data[sym].iloc[-200:].plot(ax=ax, lw2.0)


