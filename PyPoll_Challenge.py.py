# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Election-Analysis", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Election-Analysis","Analysis", "election_analysis_county.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_county = ""
winning_count = 0
winning_percentage = 0

# 1: Create a county list and county votes dictionary.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # 2: Add to the total vote count.
        total_votes += 1

        # 3: Extract the county name from each row.
        county_name = row[1]
        candidate_name = row[2]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

           # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")

    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # 6c: Calculate the percentage of votes for the county.          
        county_results = (
            f"\nCounty Votes\n"
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
         # 6d: Print the county results to the terminal.
        print(county_results, end="")

         # 6e: Save the county votes to a text file.
        txt_file.write(election_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = candidate_name
            winning_percentage = vote_percentage

            winning_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: Denver\n"
            f"-------------------------\n"
            f"Winner: {candidate_name}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

    # 7: Print the county with the largest turnout to the terminal.
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)