##The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. THe percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

import csv
import os
import datetime as dt

now = dt.datetime.now()
print("The time right now is ", now)

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_load,'r') as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)


