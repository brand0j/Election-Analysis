# Election Analysis

## Overview of Election Audit

### Purpose
The purpose of this election audit is to be able to read through election data stored within a .csv file to quickly and accurately determine the winner of the election. In addition, we would also like to know how many votes were counted, voter turnout for each county, votes cast for each candidate along with a representative percentage for each to potentially be used for future elections. Our goal is to be able to analyze this specific election, but to make something that can be easily modified and reusable for future elections varying in scope.


## Election Audit Results

### Analysis

First I began by opening the .csv file and reading in the data row-by-row using a for loop with a counter to keep track of the total votes, candidates, votes for each candidate, votes by county. This was made easier through the use of conditional if statements inside of our for loop along with dictionaries to store a vote count for each candidate & county respectively. See code below:

![csv_reader_code](https://github.com/brand0j/Election-Analysis/blob/main/Resources/csv_reader_code.PNG)

After reading through the .csv file, it was important to quickly display the vote count for each category (candidate & county) along with the winner of the elction and the county with the highest voter turnout. This was done through another comparison if statement inside a for loop that goes through the stored values of each dictionary as shown below:

![county_votes](https://github.com/brand0j/Election-Analysis/blob/main/Resources/county_votes.PNG)
![candidate_votes](https://github.com/brand0j/Election-Analysis/blob/main/Resources/candidate_votes.PNG)

Finally, we can output all the relevant information regarding the results of the election. Below you will see a breakdown that shows the total number of votes, the votes/percentage for each county, the county with the highest voter turnout, votes/percentage for each candidate, and lastly the winner of the election! You will notice that the county with the highest voter turnout is Denver by a significant margin with a total of 306,055 votes (accounting for 82.8% of the votes of the entire election). As for candidates, Diana DeGette received a total of 272,892 votes (accounting for 73.8% of the votes for the entire election) and is thus the winner of the election by a landslide.

![election_results](https://github.com/brand0j/Election-Analysis/blob/main/Resources/election_results.PNG)

## Election Audit Summary

Thankfully the code we have written is reusable for implementation in future elections since we are reading in data from a csv file. 
This could be used in a general election by switching from counties to states as long as the csv file contains election data for multiple states. 
