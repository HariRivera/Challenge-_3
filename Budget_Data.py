import csv

# Define the name of the CSV file
csv_file_name = 'budget_data.csv'

# Initialize necessary variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = []
months = []

# Open and read the CSV file using the defined file name
with open(csv_file_name, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header

    # Loop through each row in the csv
    for row in csvreader:
        total_months += 1
        total_profit_loss += int(row[1])
        
        # Calculate the change in "Profit/Losses" and add it to the list
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            profit_loss_change.append(change)
            months.append(row[0])
            
        previous_profit_loss = int(row[1])

# Calculate the greatest increase, the greatest decrease, and the average of the changes
greatest_increase = max(profit_loss_change)
greatest_decrease = min(profit_loss_change)
average_change = sum(profit_loss_change) / len(profit_loss_change)

# Find the corresponding months for the greatest increase and decrease
greatest_increase_month = months[profit_loss_change.index(greatest_increase)]
greatest_decrease_month = months[profit_loss_change.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write the results to a text file
with open('financial_analysis.txt', 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("--------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
