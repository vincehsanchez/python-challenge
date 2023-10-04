import os
import csv

csv_path = os.path.join("/Users/vincehsanchez/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv")
txtFile_path = os.path.join("/Users/vincehsanchez/Documents/GitHub/python-challenge/PyPoll/analysis/electionResults.txt")
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
total_votes = 0
winner = 'none'

with open(csv_path) as csvfile:
    csv_reader = csv.DictReader(csvfile) #Dict.Reader let everything fall into place.
    for votes in csv_reader:         
        if votes['Candidate'] == 'Charles Casper Stockham':
            candidate1_votes += 1
        if votes['Candidate'] == 'Diana DeGette':
            candidate2_votes += 1
        if votes['Candidate'] == 'Raymon Anthony Doane': 
            candidate3_votes += 1

        #vote_count
        if candidate1_votes > candidate2_votes and candidate1_votes > candidate3_votes and candidate1_votes:
            winner = "Charles Casper Stockham"        
        if candidate2_votes > candidate1_votes and candidate2_votes > candidate3_votes and candidate2_votes:
            winner = "Diana DeGette"
        if candidate3_votes > candidate1_votes and candidate3_votes > candidate2_votes and candidate3_votes:
            winner = "Raymon Anthony Doane"

    number_lines = csv_reader.line_num - 1
    total_votes = candidate1_votes + candidate2_votes + candidate3_votes
    candidate1_percent = (((candidate1_votes)/(total_votes))*100)
    candidate2_percent = (((candidate2_votes)/(total_votes))*100)
    candidate3_percent = (((candidate3_votes)/(total_votes))*100)
    total_pct = (candidate1_percent + candidate2_percent + candidate3_percent)
    #claim variables
    number_lines = (number_lines)
    total_votes = (total_votes)
    candidate1_votes = (candidate1_votes)
    candidate2_votes = (candidate2_votes)
    candidate3_votes = (candidate3_votes)
    candidate1_percent = round(candidate1_percent, 3) #https://docs.python.org/3/library/functions.html?highlight=round#round
    candidate2_percent = round(candidate2_percent, 3) #https://docs.python.org/3/library/functions.html?highlight=round#round
    candidate3_percent = round(candidate3_percent, 3) #https://docs.python.org/3/library/functions.html?highlight=round#round 
# Pretty terminal formatting
print(f"\nElection Results")
print(f"\n-------------------------")
print(f"\nTotal Votes: {total_votes}")
print(f"\n-------------------------")
print(f"\nCharles Casper Stockham: {candidate1_percent}% ({candidate1_votes})")
print(f"\nDiana DeGette: {candidate2_percent}% ({candidate2_votes})")
print(f"\nRaymon Anthony Doane: {candidate3_percent}% ({candidate3_votes})")
print(f"\n-------------------------")
print(f"\nWinner: {winner}")
print(f"\n-------------------------")
#output file
with open (txtFile_path, 'w') as txtFile: #askBCS helped me fix .txt output, did not use f string first time
    txtWriter = csv.writer(txtFile)
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Election Results"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"-------------------------"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Total Votes: {total_votes}"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"-------------------------"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Charles Casper Stockham: {candidate1_percent}% ({candidate1_votes})"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Diana DeGette: {candidate2_percent}% ({candidate2_votes})"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Raymon Anthony Doane: {candidate3_percent}% ({candidate3_votes})"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"-------------------------"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Winner: {winner}"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"-------------------------"])
    