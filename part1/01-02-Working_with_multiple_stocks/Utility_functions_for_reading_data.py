"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df2 = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
           parse_dates=True, usecols=['Date', 'Adj Close'],
           na_values='nan')

        # Rename to prevent clash
        df2 = df2.rename(columns={'Adj Close': symbol})
        df = df.join(df2)

    # Drop NaN values
    df = df.dropna()
    return df
