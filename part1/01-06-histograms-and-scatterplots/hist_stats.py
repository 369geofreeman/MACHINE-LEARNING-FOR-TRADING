# Computing histogram statistics

import pandas as pd
import matplotlib as plt

from util import get_data, plot_data


def compute_daily_returns(df):
    '''Compute and return the daily return values'''
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0  # Set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(dates, symbols)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title='Daily returns', ylabel='Daily returns', xlabel='Date')

    # Plot histogram
    daily_returns.hist(bins=20)  # Default is 10

    # Get mean and standard deviation
    mean = daily_returns['SPY'].mean()
    print("mean=", mean)
    std = daily_returns['SPY'].std()
    print("std=", std)

    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    # Compute kurtosis
    print(daily_returns.kurtosis())



if __name__ == '__main__':
    test_run()





