import os
import csv

# set initial variables and create lists
total_votes = 0
candidate_list = []
candidate_name = []
candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []

# open and read csv 
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    # loop through vote counts
    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_list.append(str(row[2])) 
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1
        elif row[2] == candidate_name[1]:
            candidate_vote[1] += 1
        elif row[2] == candidate_name[2]:
            candidate_vote[2] += 1
        elif row[2] == candidate_name[3]:
            candidate_vote[3] += 1
            
    # create functions to calculate total vote percentage
    candidate_vote_percent[0] = round(100 * (candidate_vote[0] / total_votes), 4)
    candidate_vote_percent[1] = round(100 * (candidate_vote[1] / total_votes), 4)
    candidate_vote_percent[2] = round(100 * (candidate_vote[2] / total_votes), 4)
    candidate_vote_percent[3] = round(100 * (candidate_vote[3] / total_votes), 4)

    # determine the winner
    if candidate_vote[0] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[0]
    elif candidate_vote[1] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[1]
    elif candidate_vote[2] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[2]
    elif candidate_vote[3] == max(candidate_vote[0], candidate_vote[1], candidate_vote[2], candidate_vote[3]):
       candidate_winner = candidate_name[3]

    # print election results to terminal screen
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})")
    print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})")
    print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})")
    print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})")
    print("-----------------------------")
    print(f"Winner: {candidate_winner}")

# create text file and then write election results
output_path = os.path.join("..", "Output", "Election_Results.txt")
with open(output_path, 'w', newline='') as text_file:

    print("Election Results", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"{candidate_name[0]}: {candidate_vote_percent[0]}% ({candidate_vote[0]})", file=text_file)
    print(f"{candidate_name[1]}: {candidate_vote_percent[1]}% ({candidate_vote[1]})", file=text_file)
    print(f"{candidate_name[2]}: {candidate_vote_percent[2]}% ({candidate_vote[2]})", file=text_file)
    print(f"{candidate_name[3]}: {candidate_vote_percent[3]}% ({candidate_vote[3]})", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Winner: {candidate_winner}", file=text_file)

csvfile.close()