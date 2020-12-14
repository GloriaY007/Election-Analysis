# Open the data file.
file_to_load = 'election_results.csv'
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: perform analysis.
    print(election_data)
    
#Add our dependencies
import csv
import os
# Assign a variable to load a file path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n-----------------------\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
