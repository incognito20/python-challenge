# Import standard os csv libraries
import os
import csv

#Sets filename and opens csv at given path with given csv name
filename = open('./Resources/election_data.csv', 'r')

#Creates object and maps each row to a dict
file = csv.DictReader(filename)

#Creates individual lists that correspond to each column in the election_data.csv
ballotid = []
county = []
candidate = []

#Populates each list object by iterating through each column
#Resulting lists now mirror each column of data in the csv
for col in file:
    ballotid.append(col['Ballot ID'])
    county.append(col['County'])
    candidate.append(col['Candidate'])

#Creates the output list
#Each print statement is appended as an element in the output list
#The output list will then be used to write a text file that mirrors the terminal output
output = []

#Prints the beginning of the required format to terminal and appends a duplicate to the output list
print('\n' + 'Election Results\n' + '\n' + '------------------------------' + '\n')
output.append('\n' + 'Election Results\n' + '\n' + '------------------------------' + '\n')

#Determines total votes by seeing how long the ballotid list is
VoteCount = len(ballotid)

#Prints total votes with value from line 33 and required formatting
print(f'Total Votes: {VoteCount}' + '\n')
print('------------------------------' + '\n')

#Appends the same information as elements of output
output.append(f'Total Votes: {VoteCount}' + '\n')
output.append('------------------------------' + '\n')

#Creates uniqueCandidates list and iterates through candidate list appending new candidate names
uniqueCandidates = []
for x in candidate:
    if x not in uniqueCandidates:
        uniqueCandidates.append(x)

#Sets length of uniqueCandidates to CandidateCount variable
CandidateCount = len(uniqueCandidates)

#Create indiv list to hold indiv vote totals
indiv = []

#Iterates through the candidate list and performas a count using  
#each index of the uniqueCandidates list to capture a count of votes by candidate
i = 0
while i <= CandidateCount - 1:
    x = candidate.count(uniqueCandidates[i])
    indiv.append(x)
    i = i + 1

#Creates a percent list to capture percent of vote by candidate
percent = []

#Determines number of elements in indiv to use in loop and sets variable
indivLen = len(indiv)

#Iterates through number of times using indivLen - 1 to capture individual vote totals u
#Caculates percent as answer by dividing total individual by vote total
#Sets formatanswer variable as answer formatted to two decimal places and as a percentage
#Appends formatanswer as an element to the percent list
z = 0
while z <= indivLen - 1:
    u = indiv[z]
    answer = (u / VoteCount) * 100
    formatanswer = '%.3f' % answer
    percent.append(formatanswer)
    z = z + 1

#Determines winner by maximum value in indiv list and captures the index value
#Using the index value looks up corresponding name of winner in uniqueCandiates list
maxIndiv = max(indiv)
maxIndex = indiv.index(maxIndiv)
winner = uniqueCandidates[maxIndex]

#Iterates through each uniqueCandidates list to print candidate name, percent of vote,
#individual vote total, and required formatting. Duplicate information is appended to the
#output list
i = 0
CandidateCount = len(uniqueCandidates)
while i <= CandidateCount - 1:
    newline = '\n'
    print(f'{uniqueCandidates[i]} {percent[i]}% ({indiv[i]}) {newline}')
    output.append(f'{uniqueCandidates[i]} {percent[i]}% ({indiv[i]}) {newline}')
    i = i + 1

#Print required format, winner name, and also appends each of those entries to the 
#output list.
print('------------------------------' + '\n')
output.append('------------------------------' + '\n')
print(f'Winner: {winner}' + '\n')
output.append(f'Winner: {winner}' + '\n')
print('------------------------------' + '\n')
output.append('------------------------------' + '\n')

#Using the output list opens a new text file as a text file as the name and path specified
#Writes each element of the list to that text file so that the terminal output is mirrored
# in the text file
#Closes the text file when complete
with open("./analysis/ElectionData.txt", "w") as f:
    for text in output:
        f.write(text)
        f.write('\n')
f.close()




