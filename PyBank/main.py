# Import os module to create file paths across operating systems
# Import csv module for reading CSV files
import csv
import os

# Set a path to collect the CSV data from the Resources folder
PyBankcsv = os.path.join('Resources', 'budget_data.csv')

# Open the CSV in reader mode using the path above PyBankiv
with open (PyBankcsv, newline="") as csvfile:
    
    # Specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',') 
   
    # Create header row first
    header = next(csvreader)

    monthly_count = []
    # Empty lists to store the data 
    profit = []
    profit_change = []

    # Read through each row of data after the header
    for row in csvreader:
        # populate the dates in column "monthly_count"
        monthly_count.append(row[0])

        # Append the profit information 
        profit.append(int(row[1]))
    
        #Deleted unneccesary calculations bc I'll do them in print functions

#Calculate the changes in Profit over the entire period
for i in range(len(profit)):
    # Calculate the average change in profits.
    if i < 85:
        profit_change.append(profit[i+1]-profit[i])
    
#Average of changes in Profit 
avg_change = sum(profit_change)/len(profit_change)

# Greatest increase in profit (date and amount)
greatest_increase = max(profit_change)
greatest_index = profit_change.index(greatest_increase)
greatest_date = monthly_count[greatest_index+1]

# Greatest decrease in profit (date and amount)
greatest_decrease = min(profit_change)
lowest_index = profit_change.index(greatest_decrease)
lowest_date = monthly_count[lowest_index+1]

# Print the summary table in display
# Use f-string to accept all data types without conversion
# len counts the total amount of months in column "Monthly_Count"
# sum adds up all the profits in column "Profit"
# Round the average change to two decimals

report = f"""Financial Analysis
-----------------------
Total Months:{len(monthly_count)}
Total: ${sum(profit)}
Average Change: ${str(round(avg_change,2))}
Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})
Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})"""

print (report)

# Export the file to write
output_path = os.path.join('analysis','Simplified_budget_data.txt') 
# Open the file using write mode while holding the contents in the file
with open(output_path, 'w') as txtfile: 

    # Write in this order
    txtfile.write(report)
