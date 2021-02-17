# 00-02 - Reading and Plotting Stock Data


## Lesson summary

* To read multiple stocks into a single dataframe, you need to:
* Specify a set of dates using pandas.date_range
* Create an empty dataframe with dates as index
  - This helps align stock data and orders it by trading date
* Read in a reference stock (here SPY) and drop non-trading days using pandas.DataFrame.dropna
* Incrementally join dataframes using pandas.DataFrame.join

**Once you have multiple stocks, you can:**
* Select a subset of stocks by ticker symbols
* Slice by row (dates) and column (symbols)
* Plot multiple stocks at once (still using pandas.DataFrame.plot)
* Carry out arithmetic operations across stocks, e.g. normalize by the first day's price
