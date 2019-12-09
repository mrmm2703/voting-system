# Import modules needed
import getpass
import csv

# Function to get scores from scores.csv file
def viewScores():
    # Iterate through every row in scores.csv
    with open("scores.csv", "r", newline="") as scores:
        toReturn = []
        scoresReader = csv.reader(scores)
        for i,x in enumerate(scoresReader):
            if(i != 0):
                toReturn.append([x[0], str(x[1])])
    return toReturn

# Function to add a candidate
def addCand(name):
    # Open scores.csv in append mode and add in row
    with open("scores.csv", "a", newline="") as scores:
        scoresWriter = csv.writer(scores)
        scoresWriter.writerow([name, str(0)])    

# Function to remove a candidate
def remCand(toRem):
    lines = list()
    # Open and put existing scores.csv into memory
    with open("scores.csv", "r", newline="") as csvFile:
        reader = csv.reader(csvFile)
        for i,row in enumerate(reader):
            if(i != int(toRem)):
                lines.append(row)
    # Write modified scores.csv with deleted row
    with open("scores.csv", "w", newline="") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(lines)