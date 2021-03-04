# Data import

# Working with locally stored financial data


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Specifies the file and pathname
filename = '../source/tr_eikon_eod_data.csv'

# Shoes the first five rows of the raw data
f = open(filename, 'r')
f.readlines()[:5]

# reads the file as a pandas db
data = pd.read_csv(filename,          # filename passed to read
                   index_col=0,       # Specifies that the forst column should be handled as an index
                   parse_dates=True)  # Specifies that the index values are of type datetime

# The ersulting dataframe object
data.info()

# The forst 5 rows...
data.head()

# The final 5 rows.
data.tail()

# Visualises the complete data set via multiple plots
data.plot(figsize=(10, 12), subplots=True)




