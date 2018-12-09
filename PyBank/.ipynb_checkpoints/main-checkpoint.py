import os
import csv

# define and initiate some variables
month_count = 0
date_list = []
profit_loss_list = []
total_profit_loss = float(0)
change_value_list = []
prior_value = float(0)

# path to csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# read csv file
with open(csvpath, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    #loop month count
    for value in csv_reader:
        month_count = month_count + 1
        date_list.append(str(value[0]))
        profit_loss_list.append(float(value[1]))

        current_value = value[1]
        change_value = float(current_value) - float(prior_value)
        change_value_list.append(change_value)
        prior_value = current_value

# define function and determine average change       
def average(change_value_list):
    x = len(change_value_list)
    total = sum(change_value_list) - change_value_list[0]
    avg = total / (x - 1)
    return avg

#run calculations
average_change = round(average(change_value_list), 2)
total_profit_loss = round(sum(profit_loss_list))
highest_profit_loss = round(max(profit_loss_list))
lowest_profit_loss = round(min(profit_loss_list))
highest_index = profit_loss_list.index(highest_profit_loss)
lowest_index = profit_loss_list.index(lowest_profit_loss)

# print financial summary
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_list[highest_index]} (${highest_profit_loss})")
print(f"Greatest Decrease in Profits: {date_list[lowest_index]} (${lowest_profit_loss})")

# create file to be written
output_path = os.path.join("financial_analysis.txt")
with open(output_path, "w", newline="") as text_file:

    # print to newly created file
    print("Financial Analysis", file=text_file)
    print("-------------------------------------------------", file=text_file)
    print(f"Total Months: {month_count}", file=text_file)
    print(f"Total: ${total_profit_loss}", file=text_file)
    print(f"Average Change: ${average_change}", file=text_file)
    print(f"Greatest Increase in Profits: {date_list[highest_index]} (${highest_profit_loss})", file=text_file)
    print(f"Greatest Decrease in Profits: {date_list[lowest_index]} (${lowest_profit_loss})", file=text_file)

    csvfile.close()