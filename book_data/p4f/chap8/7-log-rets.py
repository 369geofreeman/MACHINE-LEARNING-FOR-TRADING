import pandas as pd
import numpy as np

# Reads the EDO (originally from the Thomson Reuters Eikon Data API) from a CSV file
raw = pd.read_csv('../../source/tr_eikon_eod_data.csv')
data = raw[['.SPX', '.VIX']].dropna()

# When plotting (parts of) the two time series in a single plot and with adjusted scalings, the stylized fact of negative corrilation between the two indixes becomes evident through the simple visual inspection

# .loc[:DATE] selects the data until the given value DATE
data.loc[:'2012-12-31'].plot(secondary_y='VIX', flagsize=(10, 6))
