'''
Waterfall-Weighted Voting - Local CSV Storage Implementation
Author: Luke Rouleau
Last Edited: 7/11/2021
'''
#---------------------------------IMPORTS------------------------------
import csv

#---------------------------------DEFINITIONS--------------------------
def readCSV():
    with open('data.csv', newline='\n') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
#---------------------------------MAIN---------------------------------
if __name__ == "__main__":
    readCSV()
#---------------------------------UUU---------------------------------
