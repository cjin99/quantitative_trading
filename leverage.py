#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np

"""
Test leverage: 

Start from the newest values. 
Keep a minimum of the period. 

For every new investment you find, check if their SL is below the current minimum low. 
If it is lower the minimum, count as lost. 
If it is higher the minimum, then add (last_price/current_price)*investment to the amount won. 


"""

df = pd.read_csv('SP500.csv')

total_return = 0
total_invested = 0
global_minimum = 10000000
leverage = 2
invest_monthly = 500

last_price = df.values[-1][4]
months = 0
monthly_interest = 0.10/12
investments_recovered = 0
investments_lost = 0
total_interest = 0

for row in reversed(df.values):
    date = row[0]
    open = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])

    total_invested += invest_monthly

    if low < global_minimum:
        global_minimum = low

    # if the sl never gets triggered we count the investment with the last price
    sl = open - open/leverage
    if global_minimum >= sl:
        # winning
        interest_paid = months*leverage*invest_monthly*monthly_interest
        profits = (last_price/close)*invest_monthly*leverage - interest_paid
        total_return += profits
        total_interest += interest_paid
        investments_recovered += 1

        print("Investment from "+str(date)+ " of "+str(invest_monthly)+ " generated "+
                 str(profits) + " with an interest "+ str(interest_paid))
    else:
        # losing
        print("We lost this bet because the global minimum "+ str(global_minimum)+ " is lower than "+
               str(sl))
        investments_lost +=1

    months +=1


print("Total invested: "+str(total_invested))
print("Total returned: "+str(total_return))
print("Total interest: "+str(total_interest))
print("Total winning strategies: "+str(investments_recovered))
print("Total losing strategies: "+str(investments_lost))
print("Global minimum: "+str(global_minimum))
print("Total months: "+str(months))
