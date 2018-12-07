import os
import csv

bank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Lists to store data
total_months = []
net_p_l = []
average_p_l = []
increaseMax_p_l = []
increaseMax_p_l = []

# with open(bank_csv, newline="", encoding='utf-8') as csvfile:
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add total months
        len(total_months)
        total_months.append(row[1])

        # Add net profit/loss
        
        net_p_l.append(row[2])

        # Add average profit/loss
        def average(total_months)
             length = len(total_months)
             total = 0.0
             for number in total_months
                  total += retun total / length
                
        average_p_l.append(row[3])

        # Add maximum increase profit/loss
        increaseMax_p_l.append(row[4])

         # Add maximum decrease profit/loss
        increaseMax_p_l.append(row[5])

# Zip lists together
cleaned_csv = zip(total_months, net_p_l, average_p_l, increaseMax_p_l, increaseMax_p_l)

# Set variable for output file
output_file = os.path.join("bank_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Total Months", "Total Revenue", "Average Change", "Greatest Increase in Profits ()",                            "Greatest Decrease in Profits Sep-2012" ()]
                    
    # Write in zipped rows
    writer.writerows(cleaned_csv)
