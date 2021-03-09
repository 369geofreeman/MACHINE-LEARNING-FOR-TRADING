# Resampling
# ---

# Resampling is an import ant operation on financial time series data. Usually
# this takes the form of downsampling, meaning that, for exmaple, a tick data
# series is resampled to one-minute intervals or a time series with daily
# observations is resampled to one with weekly or monthly observations.

import pandas as pd
import numpy as np


filename = '../source/tr_eikon_eod_data.csv'
data = pd.read_csv(filename, index_col=0, parse_dates=True)


# EOD data gets resampled tp weekly time intervals...
data.resample('1w', label='right').last().head()

# And monthly time samples
data.resample('1m', label='right').last().head()

# And this plots the cumalative log returns over time; first the
# cumsum() method is called, then np.exp() is applied to the results, finally, the resampling takes place
rets = np.log(data / data.shift(1))
rets.cumsum().apply(np.exp).resample('1m', label='right').last().plot(figsize=(10, 6))


# Normally always use 'right' label to avoid foresight bias



