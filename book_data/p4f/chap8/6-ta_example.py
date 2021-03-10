# A Technical Analysis Example
# ---


import pandas as pd
import numpy as np

filename = '../source/tr_eikon_eod_data.csv'
data = pd.read_csv(filename, index_col=0, parse_dates=True)

# gets the data for Apple stock

sym = 'AAPL.O'
data = pd.DataFrame(data[sym]).dropna()

# Claculates the values for the shorter-term SMA (simple moving average)
data['SMA1'] = data[sym].rolling(window=42).mean()

# Calculates the values for the longer-term SMA
data['SMA2'] = data[sym].rolling(window=252).mean()

# print the last 5
print(data[[sym, 'SMA1', 'SMA2']].tail())

# Visulises theh stock price data plus the two SMA time series
data[[sym, 'SMA1', 'SMA2']].plot(figsize=(10, 6))


# In this context, the SMAs are only a means to an end. They are used to
# derive positions to implement a trading strategy. The change in position
# is triggered (visually) by a crossover of the two lines representing
# the SMA time series
# ---


# Only complete data rows are kept
data.dropna(inplace=True)

# if shorter-term SMA value is greater than the longer-term one...

data['positions'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)

# ... go long on the stock (put a 1)
# Otherwise, go short on the stock (-1)

