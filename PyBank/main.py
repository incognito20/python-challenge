# Import standard os csv libraries
import os
import csv

#Sets filename and opens csv at given path with given csv name
filename = open('./Resources/budget_data.csv', 'r')

#Creates object and maps each row to a dict
file = csv.DictReader(filename)

##Creates individual lists that correspond to each column in the budget_data.csv
months = []
result = []

#Populates each list object by iterating through each column
#Resulting lists now mirror each column of data in the csv
for col in file:
    months.append(col['Date'])
    result.append(col['Profit/Losses'])

#Creates the output list
#Each print statement is appended as an element in the output list
#The output list will then be used to write a text file that mirrors the terminal output
output = []
print('\n' + 'Financial Analysis\n' + '\n' + '------------------------------' + '\n')
output.append('\n' + 'Financial Analysis\n' + '\n' + '------------------------------' + '\n')


#Determines number of months in the analysis by the lenght of the list and sets variable
MonthCount = len(months)

#Prints total months and appends duplicate to output list
print(f'Total Months: {MonthCount}' + '\n')
output.append(f'Total Months: {MonthCount}' + '\n')

#Creates a new list equal to result but changing to type int
newformat = list(map(int, result))

#Sum of profit / losses set to total variable
total = sum(newformat)

#Prints total and appends duplicate to output list
print(f'Total: ${total}' + '\n')
output.append(f'Total: ${total}' + '\n')

#Makes a copy of the newformat list and sets name to Copy1
Copy1 = newformat.copy()

#Creates delta list
#Iterates through Copy1 subtracting profit/loss from previous month to determine difference
#Each difference is appended to delta list
delta = []
i = 0
while i < MonthCount - 1:
    x = Copy1[i + 1] - Copy1[i]
    delta.append(x)
    i = i + 1

#Calculate total difference from delta
deltaTotal = sum(delta)

#Calculate average change by dividing deltaTotal by number of months
deltaCount = len(delta)
avgDelta = deltaTotal / (MonthCount - 1)

#Formats average change to $ and two decimal points
formatDelta = '%.2f' % avgDelta

#Prints average change and appends duplicate to output list
print(f'Average Change: ${formatDelta}' + '\n')
output.append(f'Average Change: ${formatDelta}' + '\n')

#Determine minimum change in delta
minDelta = min(delta)
#Determine maximum change in delta
maxDelta = max(delta)

#Find corresponding month to greatest min and max delta using indices and the months list
minIndex = delta.index(minDelta)
maxIndex = delta.index(maxDelta)
minMonth = months[minIndex + 1] 
maxMonth = months[maxIndex + 1] 

#Print the month and value for the greatest increase and decrease in profits
print(f'Greatest Increase in Profits: {maxMonth} (${(maxDelta)})' + '\n')
print(f'Greatest Decrease in Profits: {minMonth} (${(minDelta)})' + '\n')
#Append the month and value for the greatest increase and decrease in profits to output list
output.append(f'Greatest Increase in Profits: {maxMonth} (${(maxDelta)})' + '\n')
output.append(f'Greatest Decrease in Profits: {minMonth} (${(minDelta)})' + '\n')

#Using the output list opens a new text file as a text file as the name and path specified
#Writes each element of the list to that text file so that the terminal output is mirrored
# in the text file
#Closes the text file when complete
with open("./analysis/FinancialAnalysis.txt", "w") as f:
    for text in output:
        f.write(text)
        f.write('\n')
f.close()




