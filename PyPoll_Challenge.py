
#import to read csv file
import csv
import os

#read in the csv file of the election data
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#initialize votes, candidates, and votes for each candidate dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}
counties = []
county_votes = {}

#read in the file
with open(file_to_load,'r') as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    #go through each row in the csv file
    for row in file_reader:
        
        #increment the number of votes for each row in the csv to get total_votes
        total_votes += 1
        county_name = row[1]
        candidate_name = row[2]
        

        #if statement to get unique candidate votes
        if candidate_name not in candidate_options:

            #add unique candidates to candidate_options and initialize their vote_count to 0
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #increment candidate_votes to track their total votes in the election
        candidate_votes[candidate_name] += 1



        #if statement to get the names of counties where votes were counted
        if county_name not in counties:

            #add unique counties to list of counties and initialize the vote_count to 0
            counties.append(county_name)
            county_votes[county_name] = 0
        
        #increment the number of votes for that county by 1
        county_votes[county_name] += 1
    

    #Open a txt.file to write the analysis of the election to
    with open(file_to_save,"w") as txt_file:
            
        #Header for the election results
        election_results = (
            f"\nElection Results \n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------\n\n"
            )
        print(election_results)
        txt_file.write(election_results)



        #Display the voter turnout for each county
        print(f"County Votes: \n")
        txt_file.write(f"County Votes: \n")

        winning_county = ""
        county_count = 0
        county_percentage = 0

        #Display the number of votes & percentage of the total votes for each county
        for county_name in county_votes:

            votes = county_votes[county_name]
            vote_percentage = (float((votes/total_votes)*100))

            if votes > county_count and vote_percentage > county_percentage:
                county_count = votes
                county_percentage = vote_percentage
                winning_county = county_name

            county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(county_results)
            txt_file.write(county_results)

        #Display for the county with the largest voter turnout
        voter_turnout = (
            f"\n------------------------\n"
            f"Largest County Turnout: {winning_county}"
            f"\n------------------------\n\n"
        )
        print(voter_turnout)
        txt_file.write(voter_turnout)



        #initialize for comparison to determine the winner of the election
        winning_candidate = ""
        winning_count = 0
        winning_percentage = 0

        #loop through the candidates that received votes
        for candidate_name in candidate_votes:

            #set votes & vote_percentage for each candidate
            votes = candidate_votes[candidate_name]
            vote_percentage = (float((votes/total_votes)*100))

            #comparison to determine who won the election w/number of votes and their percentage of the total votes
            if votes > winning_count and vote_percentage > winning_percentage:

                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

            #prints each candidate and their corresponding votes & vote_percentage for the election
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)



        #output for the winner of the election
        winning_candidate_summary = (
            f"\n---------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------\n"
        )

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)




