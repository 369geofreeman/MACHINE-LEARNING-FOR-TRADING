"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/IBM.csv")
    # TODO: Your code here
    plt.title('High prices for IBM')
    plt.plot(df['High'][::-1])
    plt.ylabel('Daily high')
    plt.xlabel('Date')
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
