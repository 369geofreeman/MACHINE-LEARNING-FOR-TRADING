# Calculating the sharpe ratio


# Overview
# ---

# used to help investors understand the return of an investment compared to its risk.1

# The ratio is the average return earned in excess of the risk-free rate per unit of volatility or total risk. Volatility is a measure of the price fluctuations of an asset or portfolio.
#
# Subtracting the risk-free rate from the mean return allows an investor to better isolate the profits associated with risk-taking activities. The risk-free rate of return is the return on an investment with zero risk, meaning it's the return investors could expect for taking no risk. The yield for a U.S. Treasury bond, for example, could be used as the risk-free rate.
#
# Generally, the greater the value of the Sharpe ratio, the more attractive the risk-adjusted return.


# Formula
# ---

#               Rp - Rf
# Sharp Ratio =  -----
#                 σp 

# Where:
#    Rp = return of portfolio
#    Rf = risk-free rate
#    σp = standard deviation of the portfolios excess return


# Code:
import math

avg_daily_ret = 10
daily_risk_free = 2
std_daily_ret = 10

print(math.sqrt(252) * ((avg_daily_ret - daily_risk_free) / std_daily_ret))









