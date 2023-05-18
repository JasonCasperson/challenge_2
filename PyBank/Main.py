import pandas as pd
import os
import csv
import numpy as np
from pathlib import Path
import datetime
change = []
financials_csv = Path('PyBank/Resources/budget_data.csv')
fileFrame = pd.read_csv(financials_csv)
fileFrame['Date'] = pd.to_datetime(fileFrame['Date'],format='%b-%y')
MinDate = fileFrame['Date'].min()
MaxDate = fileFrame['Date'].max()
DateRange = round((MaxDate - MinDate)/np.timedelta64(1, 'M'))
TotalRevenue = fileFrame['Profit/Losses'].sum()
totalvolume = 0
greatestincrease = 0
greatestdecrease = 0
print(fileFrame.columns)

for i in range(len(fileFrame.index)):
    
    totalvolume += int(fileFrame.iloc[i,1])

    if int(fileFrame.iloc[i,1]) > greatestincrease:
        BestMonth = fileFrame.iloc[i,0]
        greatestincrease = int(fileFrame.iloc[i,1])
    elif int(fileFrame.iloc[i,1])<greatestdecrease:
        worstMonth = fileFrame.iloc[i,0]
        greatestDecrease = int(fileFrame.iloc[i,1])
    change.append(int(fileFrame.iloc[i,1]))

monthly_change = pd.Series(change)
AverageChange = monthly_change.mean()

print(f"Total Months: {DateRange}")
print(f"Total: ${TotalRevenue}")
print(f"Average Change: ${AverageChange}")
print(f"Greatest Increase in Profits: {BestMonth} (${greatestincrease})")
print(f"Greatest Decrease in Profits: {worstMonth} (${greatestDecrease})")

textfile = open(Path('PyBank/Resources/txtoutput.txt'),'w')
print(f"Total Months: {DateRange}",file=textfile)
print(f"Total: ${TotalRevenue}",file=textfile)
print(f"Average Change: ${AverageChange}",file=textfile)
print(f"Greatest Increase in Profits: {BestMonth} (${greatestincrease})",file=textfile)
print(f"Greatest Decrease in Profits: {worstMonth} (${greatestDecrease})",file=textfile)




