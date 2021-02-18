# Compute-global-statistics


import numpy as np
import pandas as pd
import matplotlib as plt


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title=""):
    '''Plot stock prices with a custom title and a meaningful axis label'''
    ax = plot(title=title, fontSize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    # Read data
    dates = pd.date_range('2010-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute global statistics for each stock

    # sum of all divided by length
    print(df.mean())
    # middle price when list is sorted
    print(df.median())
    # how much the members of a group differ from the mean value for the group.
    print(df.std())


if __name__ == '__main__':
    text_run()


