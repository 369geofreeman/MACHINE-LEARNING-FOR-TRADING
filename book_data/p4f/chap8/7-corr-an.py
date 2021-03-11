# Correlation Analysis
# ---


# In the case of the S&P 500 stock index and the VIX volatillity index, It is
# a stylized fact that when the S&P rises, the VIX falls in general, and
# vice verca. this is about correlation and not causation.
# Here we will come up with some supporting statistical evidence for the stylized
# face that the S&P 500 and the VIX are (highly) negatively correlated


import pandas as pd
import numpy as np

# Reads the EDO (originally from the Thomson Reuters Eikon Data API) from a CSV file
raw = pd.read_csv('../../source/tr_eikon_eod_data.csv')
data = raw[['.SPX', '.VIX']].dropna()

# When plotting (parts of) the two time series in a single plot and with adjusted scalings, the stylized fact of negative corrilation between the two indixes becomes evident through the simple visual inspection

# .loc[:DATE] selects the data until the given value DATE
data.loc[:'2012-12-31'].plot(secondary_y='VIX', flagsize=(10, 6))





