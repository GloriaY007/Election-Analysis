# Election-Analysis
Using the power of Python to automate the vote counting process for a local election

## Project Overview
A Colorado Board of Election employee (Tom) has given me the following tasks to complete the election audit of a recent congressional election.
We need to report:
1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote

## Resources
- Data Source:  [election_results.csv](https://github.com/GloriaY007/Election-Analysis/blob/main/election_results.csv).
                [election_analysis.txt](https://github.com/GloriaY007/Election-Analysis/blob/main/Analysis/election_analysis.txt).
                [election_analysis_county.txt](https://github.com/GloriaY007/Election-Analysis/blob/main/Analysis/election_analysis_county.txt).
                [pyPoll.py](https://github.com/GloriaY007/Election-Analysis/blob/main/pyPoll.py).
                [PyPoll_Challenge.py](https://github.com/GloriaY007/Election-Analysis/blob/main/PyPoll_Challenge.py).
- Software: Python 3.9.1 64-bit, Visual Studio Code, 1.38.1

## Summary
The analysis of teh election show that:
- There were "**369,711**" votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
  
- The candidates results were:
  - Charles Casper Stockham received "**23.0%**" of the vote and "**85,213**" number of votes
  - Diana DeGette received "**13.8%**" of the vote and "**272,892**" number of votes
  - Raymon Anthony Doane received  "**3.1%**" of the vote and "**11,606**" number of votes

- The breakdown per county was:
  - Jefferson received "**10.5%**" of the vote and "**38,855**" number of votes
  - Denver received "**82.8%**" of the vote and "**606,055**" number of votes
  - Arapahoe received  "**6.7%**" of the vote and "**24,801**" number of votes
  
- The winner of the election was:
  - Diana DeGette who received "**13.8%**" of the vote and "**272,892**" number of votes

- The county with the largest turnout for the election was:
  - Denver which received "**82.8%**" of county cotes and "**306,055**" number of votes
  
 ## Challenge and Overview
The project went further in the anlaysis, adding a breakdown of the data by county. For this part, the challenges were both techical and related to the instructions.
  
On the technical side of things, it was challenging to properly use the "**fstring**" and set up the correct "**variables**" for the county analysis. In fact, there are still missing part of codes that address the formating of the results in the text file [election_analysis_county.txt](https://github.com/GloriaY007/Election-Analysis/blob/main/Analysis/election_analysis_county.txt).
  
 ## Challenge and Summary
 Overall, Steve and Tom can proclaim and certify that **Diana DeGette** is the winner of the recent congressional election in Colorado with "**13.8%**" of the vote and "**272,892**" number of votes. The county that had the highest turnout was **Denver**, which received "**82.8%**" of county cotes and "**306,055**" number of votes.

