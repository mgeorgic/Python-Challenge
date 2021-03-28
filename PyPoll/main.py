#Import Modules
import os 
import csv

# Set a path to collect the CSV data from the Resources folder
pypollcsv = os.path.join('Resources', 'election_data.csv')

# Empty Lists to store data in and a counter for total votes 
candidates = []
number_voters = []
percent_votes = []
total_votes = 0

# Open the CSV in reader mode using the path above PyPollcsv
with open (pypollcsv, newline="") as csvfile:
    
    # Specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # The file has a header so skip it
    header = next(csvreader)

    # for loop to find unique candidate names
    for row in csvreader:
        # Count in votes
        total_votes = total_votes + 1 
		
        #Find the list of candidates 
        if row[2] not in candidates:
            candidates.append(row[2])
    
    print(f'List of candidates: {candidates}')

# for loop to calculate votes
with open(pypollcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    # Candidate counters
    khan_voters = 0
    correy_voters = 0
    li_voters = 0
    otooley_voters = 0

    # Read through each row of data after the header
    for row in csvreader:
    
    # Calculate each candidate's number of votes
        if row[2] == candidates[0]:
            khan_voters = khan_voters + 1
        elif row[2] == candidates[1]:
            correy_voters = correy_voters + 1
        elif row[2] == candidates[2]:
            li_voters = li_voters + 1
        elif row[2] == candidates[3]:
            otooley_voters = otooley_voters + 1
   
    # Calculate Percentage Of Votes Each Candidate Won
    kahn_percent = khan_voters / total_votes
    correy_percent = correy_voters / total_votes
    li_percent = li_voters / total_votes
    otooley_percent = otooley_voters / total_votes
    
    # Calculate total voters
    total_votes = khan_voters + correy_voters + li_voters + otooley_voters
    
    # Calculate Winner Of The Election Based On Popular Vote
    winner = max(khan_voters, correy_voters, li_voters, otooley_voters)

    if winner == khan_voters:
        winner_name = "Khan"
    elif winner == correy_voters:
        winner_name = "Correy"
    elif winner == li_voters:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 
        
# Print Answers
# Range 0:.3% gives you accuracy
# F-String allows for all data types
# Print tests

report = f"""Election Results
-------------------------------------
Total Votes: {total_votes}
-------------------------------------
Kahn: {kahn_percent:.3%}({khan_voters})
Correy: {correy_percent:.3%}({correy_voters})
Li: {li_percent:.3%}({li_voters})
O'Tooley: {otooley_percent:.3%}({otooley_voters})
-------------------------------------
Winner: {winner_name}
-------------------------------------"""

# Export the file to write
output_path = os.path.join('analysis','Simplified_election_data.txt') 
# Open the file using write mode while holding the contents in the file
with open(output_path,'w') as txtfile: 
    
    # Write text file in the above order
    txtfile.write(report)