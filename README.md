# Challenge_3

Overview
This repository contains Python scripts designed to automate the analysis of financial records (PyBank) and election results (PyPoll). 
These scripts are capable of parsing large datasets from CSV files to generate comprehensive summaries of the data, which are both printed to the terminal and saved to text files for easy access and review.

PyBank
Objective
The PyBank script analyzes financial records to provide insights into the company's financial performance over a period. It processes data from a CSV file named budget_data.csv, which contains two columns: "Date" and "Profit/Losses".

Key Calculations
The script calculates:

The total number of months included in the dataset.
The net total amount of "Profit/Losses" over the entire period.
Changes in "Profit/Losses" over the period and the average of those changes.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in profits (date and amount) over the entire period.
Results
Results are printed to the terminal and exported to a text file named financial_analysis.txt, summarizing the financial health and notable fluctuations in the company's financial records.

PyPoll
Objective
The PyPoll script helps in modernizing the vote-counting process for a small, rural town by analyzing election data. It processes data from a CSV file named election_data.csv, which consists of three columns: "Voter ID", "County", and "Candidate".

Key Calculations
The script calculates:

The total number of votes cast in the election.
A complete list of candidates who received votes.
The percentage of votes each candidate won.
The total number of votes each candidate won.
The winner of the election based on popular vote.
Results
Results are printed to the terminal and exported to a text file named election_results.txt, providing a detailed summary of the election outcomes, including vote percentages and the overall winner.

Usage
To run these scripts, ensure you have Python installed on your system. Place the CSV files (budget_data.csv for PyBank and election_data.csv for PyPoll) in the same directory as the scripts. Open a terminal in this directory and run:

For PyBank: python pybank_script.py

For PyPoll: python pypoll_script.py

Conclusion

These Python scripts provide an automated solution to analyze financial records and election data efficiently, offering quick insights into the datasets with minimal manual intervention. They are adaptable for similar datasets and can be customized for more detailed analysis as required.
