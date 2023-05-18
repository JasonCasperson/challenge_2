import pandas as pd
import os
import csv
import numpy as np
from pathlib import Path
import datetime
textfile = open(Path('PyPoll/Resources/txtoutput.txt'),'w')
candidates = []
results_csv = Path('PyPoll/Resources/election_data.csv')
fileFrame = pd.read_csv(results_csv)
totalvotes = len(fileFrame)
winner = ""
greatestpercentage = 0
candidates = fileFrame["Candidate"].unique()
print(f"Total # of votes: {totalvotes}")
print(f"Total # of votes: {totalvotes}",file=textfile)
for i in range(len(candidates)):
    candidatevotes = len(fileFrame.loc[fileFrame['Candidate'] == candidates[i],:])
    candidatepercentage = (candidatevotes/totalvotes)*100

    
    if candidatepercentage > greatestpercentage:
        winner = candidates[i]
        greatestpercentage = candidatepercentage
    print(f"{candidates[i]}: {candidatepercentage}%")
    print(f"{candidates[i]}: {candidatepercentage}%",file = textfile)

print(f"Winner: {winner}")
print(f"Winner: {winner}",file=textfile)
   


