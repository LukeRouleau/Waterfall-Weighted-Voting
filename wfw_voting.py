'''
Waterfall-Weighted Voting - Local CSV Storage Implementation
Author: Luke Rouleau
Last Edited: 7/11/2021

Possible Extentions: Using Pandas Dataframe for the data
                    Make this into a discord bot for movie clubs and such
                    Need to Finish the prompting I/O
'''
#---------------------------------IMPORTS------------------------------
import csv
from os import read
import sys
import pandas as pd
#---------------------------------DEFINITIONS--------------------------
def readCSV(file):
    '''A non-pandas read-function'''
    with open(file, newline='\n') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def pdReadCSV(file):
    '''A pandas read-function to dataframe'''
    df = pd.read_csv(file)
    return df

def addMember(df,member):
    #df.append(pd.DataFrame([[6,"d"]],columns=df.columns)).sort_values('foo').reset_index(drop=True)
    newDF = df.append(pd.DataFrame([[member,'~','~','~']],columns=df.columns)).sort_values('member').reset_index(drop=True)
    return newDF

def removeMember(df,member):
    #df.drop(df.loc[df['Stock']=='Yes'].index, inplace=True)
    newDF = df.drop(df.loc[df['member']==member].index).reset_index(drop=True)
    return newDF

def addNom(df,member,nom,author):
    '''Add a nomination for a user. Sets the waterfall votes to 0. Replaces the nom if one exists already.'''
    df.loc[df['member'] == member, ['curr_nom','author','waterfall']] = [[nom,author,'0']]
    return df

def addNomFromInput(df,member):
    '''Prompt the user for a nomination and receive the input'''
    res = '0'
    while(1):
        res = input('Since ' + member + ' won last cycle, are they choosing a new nomination?\n\t(N)\tNo\n\t(Y)\tYes\n\t')
        if(res.lower() == 'n'):
            # Empty insert
            print('Adding ' + member + "'s selection {~, ~} to the table.")
            addNom(df, member, '~', '~')
            break
            
        elif(res.lower() == 'y'):
            nom = input('Type the name of the nomination ' + member + ' selected:\n\t')
            auth = input('Type the name of the author ' + member + ' selected:\n\t')
            print('Adding ' + member + "'s selection {" + nom + ', ' + auth + '} to the table.')
            addNom(df, member, nom, auth)
            break
    return

def memberFromIndex(df,index):
    return df.loc[index]['member']

def cycle(df):
    '''A Voting Cycle'''
    # Initiating a Vote Cycle
    
    # Would anyone else like to change their nom? This will reset their waterfall votes
    # Incrementing waterfall votes...Done
    res = '0'
    while (1):
        res = input("Type your selection and hit enter:\n\t(0)\tInitiate a new selection cycle\n\t(E)\tExit\n\t")
        if res.lower() == 'e':
            sys.exit("Goodbye, have a good read!")
        if res == '0':
            break
        else:
            print('Make a valid selection.')

    # Selection cycle has been initiatied
    print('\nThis is the current data spreadsheet:\n')
    print(df)
    print('\n')
    while (1):
        res = input("Type the index of the row which won the vote last cycle\n\t")
        try:
            res = int(res)
            member = memberFromIndex(df,int(res))
            addNomFromInput(df,member)
        except ValueError:
            print('Make a valid selection.')
        

    # Since ___ won last cycle, what is their new nom?

    return 0 



#---------------------------------MAIN---------------------------------
if __name__ == "__main__":
    df = pdReadCSV('data.csv')
    print (df)
    # Choose (Cycle, Add member, remove member, exit)
    print('\n')
    cycle(df)
#---------------------------------UUU---------------------------------
