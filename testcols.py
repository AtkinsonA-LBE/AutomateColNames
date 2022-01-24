from os import name
from sqlite3 import Date
from tkinter.messagebox import IGNORE
import pandas as pd
import numpy as np
import re
from dateutil.parser import parse
import datetime
 #Variable-------------

CSV1 = r'C:\Users\charl\OneDrive\Documents\Python Projects\BudgetForLife-Automation\CVSFile_CheckFunction\activity.csv'

Date_Column = 'Date'
Account_Column = 'Account #'
df = pd.read_csv(CSV1, header=0, names=None)
df = pd.DataFrame(df)


try:
    df.columns = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6']
    print(df.head())
except ValueError:
    df.columns = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5']
    print('1')
else:
    pass # do nothing
try:
    print(df.head())
except ValueError:
    df.columns = ['Col1', 'Col2', 'Col3', 'Col4']
    print('2')
else:
    pass #do nothing
try:
    print(df.head())
except ValueError:
    df.columns = ['Col1', 'Col2', 'Col3']
    print('3')
try:
    print(df.head())
except ValueError:
    print('4')
else:
    pass #do nothing
#trying to locate trialPD4 column name
trialPD4 = df.iloc[:,3] #fourth colmun (Account #)
print(trialPD4.name)

#Determine if column debit or credit column; 1) is float?, 2) is -? => credit, 3) is +? => debit 
#try: 

def CheckFloat(x):
    #x = trialPD4[0:3]
    for item in x:
        if isinstance(item, float):
            
            #print('Is a float.')
            #x.name = 'Float'
            #print(x.name)
            print(item)
            #return True
            if item > 0:
                x.name = 'Debit'
                print(x.name)
            elif item < 0:
                x.name = 'Credit'
                print(x.name)
                pass
            #b = item*-1
            #if isinstance(b, float):
               
            #    x.name = 'Credit'
            #    print(x.name)
            #    print(b)
            #else:
            #    pass #do nothing
        else:
            print('Is not a float.')
            #print(abs(x))
            pass #do nothing
            return False
            
trialPD5 = df.iloc[:,4] #fifth column (Amount)
CheckFloat(trialPD5) #verifies amount is float
CheckFloat(trialPD4) #verifies account # column is not a float
#print((trialPD5[0:1])*-1) 