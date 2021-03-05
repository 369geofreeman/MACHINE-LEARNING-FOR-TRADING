# Changes over time
# ---

# Statistical analysis methods are often based on chages over time and not
# the absolute values themselves. There are multiple options to calculate
# the changes in a time series over time, including absolute differences,
# percentage changes, and logrithimic (log) returns.


# import the libraries and data

import pandas as pd
import numpy as np


filename = '../source/tr_eikon_eod_data.csv'
data = pd.read_csv(filename, index_col=0, parse_dates=True)


# diff() provides the absolute changes between two index values
data.diff().head()

# Aggregation operations can be applied in addition
data.diff().mean()

# Percentage changes are prefered

# cpt_change() calculates the percentage change between two index values
data.pct_change().round(3).head()

# We can also visualise the results as a bar plot
data.pct_change().mean().plot(kind='bar', figsize=(10, 6))



# log returns
# ---

#  Calculates the log returns in vectorized fashion
rets = np.log(data / data.shift(1))

# A subset of the results
rets.head().round(3)

# Plots the cumulative log returns over time; forst the cumsum() method is called,
# Then np.exp() is applied top teh results

rets.cumsum().apply(np.exp).plot(figs=(10, 6))


