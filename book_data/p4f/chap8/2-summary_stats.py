# Summary Statistics
# ---

# The next the financial analyst might take is to have a look at different 
# summery statistics for the data set to get a 'feeling' for what it's all about:


import pandas as pd
import numpy as np


filename = '../source/tr_eikon_eod_data.csv'
data = pd.read_csv(filename, index_col=0, parse_dates=True)

# info() gives some metainformation about the dataframe object
data.info()

# describe() provides useful standard statistics per column
data.describe()

# To get specific statistics per column you can call them:
# ---

# mean()
data.mean()

# We can can also call multiple options for the dataframe

print(data.aggregate([min,
                      np.mean,
                      np.std,
                      np.median,
                     max]
                    ).round(2))



