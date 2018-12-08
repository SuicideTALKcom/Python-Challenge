import os
import csv

total_votes = 0
candidate_list = []
candidate_name = []
candidate_vote = [0, 0, 0, 0]
candidate_vote_percent = [0, 0, 0, 0]
candidate_winner = []

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r+', newline='') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_list.append(str(row[2])) 
        
    for row[2] in candidate_list:
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
        if row[2] == candidate_name[0]:
            candidate_vote[0] += 1