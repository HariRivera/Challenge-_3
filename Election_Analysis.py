import csv

# Define the name of the CSV file
csv_file_name = 'election_data.csv'

# Initialize necessary variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Open and read the csv file
with open('election_data.csv', mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header

    # Iterate through each row in the csv
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the winner and percentages
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (votes, percentage)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, (votes, percentage) in candidates.items():
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write the results to a text file
with open('election_results.txt', 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate, (votes, percentage) in candidates.items():
        textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")
