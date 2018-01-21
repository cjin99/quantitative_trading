# Introduction

This is a repository where I choose to share some basic tests for quantitative trading or stock market analysis. Notice that the most elaborated will not be made public.

These scripts are usually written in Python3, use Numpy and Pandas.  These all use real data from the stock market.

It is assumed some basic knowledge of finantial markets and basic Python programming skills. 

# Test leverage: 

Backtesting of a simple trading strategy using a variable amount of leverage on the S&P 500, with constant contributions during a period of 30 years. 

General strategy:

- Start from the newest values. 
- Keep a minimum of the period. 

For every new investment you find, check if their Stop Loss is below the current minimum low:

- If it is lower the minimum, count as lost. 
- If it is higher the minimum, then add (last_price/current_price)*investment to the amount won. 

Notice top Loss is calculated as a function of the leverage. If the leverage is 2x, the stop loss will be placed roughly at 50%, if the leverage is 3x the stop loss will be placed at 33% below the buying price and so on. 

# Leverage example

The following is an example with: 

	leverage = 2
	invest_monthly = 500
	monthly_interest = 0.10/12 

 python3 leverage.py output:
 
	Investment from 2017-10-01 of 500 generated 1000.0 with an interest 0.0
	Investment from 2017-09-01 of 500 generated 10041707586131433 with an interest 8.333333333333334
	Investment from 2017-08-01 of 500 generated 1016.7231124026936 with an interest 16.666666666666668
	Investment from 2017-07-01 of 500 generated 1011.5541081991446 with an interest 25.0
	Investment from 2017-06-01 of 500 generated 1024.5352336277372 with an interest 33.333333333333336
	Investment from 2017-05-01 of 500 generated 1022.8048518838281 with an interest 41.666666666666664
	Investment from 2017-04-01 of 500 generated 1029.451327202253 with an interest 50.0

[...]
Period from 1988 until 2017 omitted to save space. 
Run the script to see the complete output.


	Investment from 1988-06-01 of 500 generated 14834.63422640061 with an interest 2933.3333333333335
	Investment from 1988-05-01 of 500 generated 15641.577978561962 with an interest 2941.6666666666665
	Investment from 1988-04-01 of 500 generated 15793.711844063753 with an interest 2950.0
	Investment from 1988-03-01 of 500 generated 15992.80569675219 with an interest 2958.3333333333335
	Investment from 1988-02-01 of 500 generated 15398.665239156953 with an interest 2966.6666666666665
	Investment from 1988-01-01 of 500 generated 16247.005766799994 with an interest 2975.0

Global results: 

	Total invested: 179000
	Total returned: 1265035.6451023833
	Total interest: 518491.6666666667
	Total winning strategies: 344
	Total losing strategies: 14
	Global minimum: 242.86999500000002
	Total months: 358

As you can see the results are very good for long periods of time. Feel free to play with higher leverage, different interest rates and different monthly additions. 

