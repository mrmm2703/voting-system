# Impport modules
import csv

def openScores():
    # Open scores.csv in read mode and read into memory
    readCsv = open("scores.csv", "r", newline="")
    reader = csv.reader(readCsv)
    lines = list()
    # Loop and print every row except the first row (index 0)
    for i, value in enumerate(reader):
        lines.append(value)
        if i == 0:
            continue
    return lines
    
def updateVotes(lines, choice):
    # Rewrite scores.csv with updated votes and save
    with open("scores.csv", "w", newline="") as csvFile:
        writer = csv.writer(csvFile)
        for i, value in enumerate(lines):
            if int(i) == int(choice):
                writer.writerow([value[0], int(value[1]) + 1])
            else:
                writer.writerow(value)
