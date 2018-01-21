# Introduction

This is a repository where I choose to share some of my most basic tests for quantitative trading or stock market analysis. Notice that the most elaborated will not be made public.

These scripts are usually written in Python3, use Numpy and Pandas.  These all use real data from the stock market.

It is assumed some basic knowledge of finantial markets and basic Python programming skills. 

# Test leverage: 

Tests a simple strategy using leverage on the S&P 500. 

General strategy:

- Start from the newest values. 
- Keep a minimum of the period. 

For every new investment you find, check if their Stop Loss is below the current minimum low:

- If it is lower the minimum, count as lost. 
- If it is higher the minimum, then add (last_price/current_price)*investment to the amount won. 

Notice top Loss is calculated as a function of the leverage. If the leverage is 2x, the stop loss will be placed roughly at 50%, if the leverage is 3x the stop loss will be placed at 33% below the buying price and so on. 