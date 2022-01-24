from sqlite3 import Date
from tkinter.messagebox import IGNORE
from tokenize import Name
from unicodedata import name
from xmlrpc.client import _datetime_type
import pandas as pd
import numpy as np
import re
from dateutil.parser import parse
import datetime
 #Variable-------------

CSV1 = r'C:\Users\charl\OneDrive\Documents\Python Projects\BudgetForLife-Automation\CVSFile_CheckFunction\activity.csv'

df = pd.read_csv(CSV1, header=0, names=None)
df = pd.DataFrame(df)
#----------------Rename columns based on number of actual columns--------------
#Edit later to nest try except so df.head is only printed once when print(df.head()) is true
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

#print(df.head())
##print(df.iloc[0:0]) ----> Returned: Row 1 with column names
#df['Date'] = np.where(df.iloc[0:0].str.contains(, flags = re.IGNORECASE))

#print(df.columns[0]) ------> Returned: Date
#print(df.iloc[:,0]) ------> Returned: First column (dates) see: https://www.shanelynn.ie/pandas-iloc-loc-select-rows-and-columns-dataframe/
#print(df.iloc[0:1,0:1]) -----> Returned (first row and first column, this reads index[0]:row[1], index[0],col[1]):            Date
#                                                                                                                       0      12/31/2021
#print(df.iloc[0:1,0]) ------> Returned(reads index[0]:row[1], index[0]): 0   12/31/2021
trialPD2 = df.iloc[:,1] #second column (Description)
trialPD1 = df.iloc[:,0] #first column (Dates)
trialPD5 = df.iloc[:,4] #fifth column (Amount)
trialPD4 = df.iloc[:,3] #fourth colmun (Account #)
trialPD3 = df.iloc[:,2] #third column (Card Member)
##trialPD1 = pd.to_datetime(trialPD1, errors='coerce').ffill()
##trialPD2 = pd.to_datetime(trialPD2, errors='coerce').ffill()
#print(trialPD) ----> Returned: 0     2021-12-31
#print(trialPD1) ---> Returned: ValueError
#df['Col1'] = trialPD1

#----------------------------------------

#Next, evaluate each column to determine if is a date, if ValueError is raised = Not a date, if no ValueError = date
##def CheckDate(f): #Failed Date colunm assignment, for some unknown reason couldnt make this into a function and also define the f.name as 'Date', outside of the function trialPD1.name kept returning 'Col1'
##    try:
##        f = pd.to_datetime(f, errors='raise').ffill()
        #f.name = 'Date'
##        print(f)
##        print(f.dtype)
##       if f.dtype == datetime.date:
##            print('hi')
        #for item in f:
            #if isinstance(item, datetime.date):
                
            #    f.name = 'Date'
            #    print('Date column set.')
            #    return True
            #else:
            #    pass
##    except ValueError:
##        pass #do nothing
    #else:
        #a.name = 'Date'
        #print('"Date" column set.')
    #    pass

for item in trialPD1:
    if isinstance(item, int):
        break
    if isinstance(item, float):
        break
    else:
        #continue
        try:
            trialPD1 = pd.to_datetime(trialPD1, errors='raise').ffill()
        except ValueError:
            pass #do nothing
        else:
            trialPD1.name = 'Date'
            trialPD1 = trialPD1.astype('object')
            #print('1')
for item in trialPD2:
    if isinstance(item, int):
        break
    if isinstance(item, float):
        break
    else:
        #continue
        try:
            trialPD2 = pd.to_datetime(trialPD2, errors='raise').ffill()
        except ValueError:
            pass #do nothing
        else:
            trialPD2.name = 'Date'
            trialPD2 = trialPD2.astype('object')
            #print('2')
for item in trialPD3:
    if isinstance(item, int):
        break
    if isinstance(item, float):
        break
    else:
        #continue
        try:
            trialPD3 = pd.to_datetime(trialPD3, errors='raise').ffill()
        except ValueError:
            pass #do nothing
        else:
            trialPD3.name = 'Date'
            trialPD3 = trialPD3.astype('object')
            #print('3')
for item in trialPD4:
    if isinstance(item, int):
        break
    if isinstance(item, float):
        break
    else:
        #continue
        try:
            trialPD4 = pd.to_datetime(trialPD4, errors='raise').ffill()
        except ValueError:
            pass #do nothing
        else:
            trialPD4.name = 'Date'
            trialPD4 = trialPD4.astype('object')
            #print('4')
for item in trialPD5:
    if isinstance(item, int):
        break
    if isinstance(item, float):
        break
    else:
        #continue
        try:
            trialPD5 = pd.to_datetime(trialPD5, errors='raise').ffill()
        except ValueError:
            pass #do nothing
        else:
            trialPD5.name = 'Date'
            trialPD5 = trialPD5.astype('object')
            #print('5')

print(trialPD1.name) #verifies only trialPD1 can be converted to a date as an object, not as interger or float
print(trialPD2.name)
print(trialPD3.name)
print(trialPD4.name)
print(trialPD5.name)

#-----------------------------------

#Determine if column is 'Account #' column, by determining if int.
def CheckInt(c):
    for item in c:
        n = isinstance(item, int)
        if n:
            print('Is int.')
            #print(c)
            if n == True: 
                n = c
                c.name = 'Account #'
                break
            else:
                pass
        else:
            #print('Is not a int.')
            pass #do nothing

CheckInt(trialPD1)
CheckInt(trialPD2)
CheckInt(trialPD3)
CheckInt(trialPD4)#verifies trialPD4 is an int
CheckInt(trialPD5)
#print(trialPD4[0:3].to_string(index=False))

try:
    'Account #'
except NameError:
    pass #do nothing
else:
    print('"Account #" column set.')

#Determine if column debit or credit column; 1) is float?, 2) is -? => credit, 3) is +? => debit 
def Create_DF(y):
        y_data = {'Debit': [y]} 
        df_item = pd.DataFrame(y_data)
        print(df_item)
        return df_item

def CheckFloat(x):
    for item in x:
        if isinstance(item, float):
            print(item)            #prints item, that is a float
            if item > 0:
                x.name = 'Debit'
                print(x.name)      #then assigns and prints column name as 'Debit' if item > 0
                Create_DF(item)
            elif item < 0:
                x.name = 'Credit'  #or assigns and prints column name as 'Credit' if item < 0
                print(x.name)
                pass
        else:
            #print('Is not a float.') #passes if column is not a float
            pass #do nothing
            #return False

CheckFloat(trialPD4) #verifies account # is not float
CheckFloat(trialPD1) #verifies is not float
CheckFloat(trialPD2) #verifies is not float
CheckFloat(trialPD3) #verifies is not float
CheckFloat(trialPD5) #verifies amount is float
#while trialPD5.name == 'Debit':
#    New_Column = trialPD5
#while trialPD5.name == 'Credit':
#    New_Column1 = trialPD5
#print(New_Column)
#print(New_Column1)
print('Debit and Credit Columns assigned')
print(trialPD5.items())

#Determine if column is the 'Amount Name' or 'Card Member' column
Account_Name = input('Checking account names: What is the first or last name on the account? ')
Account_Name = Account_Name.lower().strip()
More_accounts = input ('Anymore accounts (If there are more than one name on a bank statement answer yes)? (yes/no) ')
if More_accounts.lower().strip() == 'yes':
    Account_Name2 = input('What is the second account name? ')
    Account_Name2 = Account_Name2.lower().strip() 
else:
    pass #Do nothing

def CheckAccount(b):
    if Account_Name in b[0].lower().strip():
    #Accounts (i.e Account_Name) in trialPD4[0].lower().strip(): ---> returned: 'Is an account.'
    #Account_Name in trialPD4[0:3].to_string(index=False).lower().strip(): ----> returned: 'Is an account.'
        #print('Account_Name is an account.')
        b.name = 'Account Name'
        print(b.name)
        #print(b[0:3])
        print('Account Column is set.')
    else:
        pass #Do nothing
    try:
        Account_Name2
        if Account_Name2 in b[0].lower().strip():
            #print('Account_Name2 an account.')
            b.name = 'Account Name'
            print(b.name)
            #print(b[0:3])
            print('Account Column is set.')
        else:
            pass #do nothing
    except NameError:
        pass #do nothing
#if Account_Name in trialPD3[0].lower().strip(): #Successful Account Name identification, however, wasnt a function so it wasnt used
    #Accounts (i.e Account_Name) in trialPD4[0].lower().strip(): ---> returned: 'Is an account.'
    #Account_Name in trialPD4[0:3].to_string(index=False).lower().strip(): ----> returned: 'Is an account.'
    #convert series string into string: x[1:2].astype(str).str
#    print('Account_Name is an account.')
#else:
#    pass #Do nothing

#try:
#    Account_Name2
#    if Account_Name2 in trialPD3[0].lower().strip():
#        print('Account_Name2 an account.')
#    else:
#        pass #do nothing
#except NameError:
#    pass #do nothing
try:
    CheckAccount(trialPD1)
except AttributeError:
    pass #do nothing
try:
    CheckAccount(trialPD2)
except AttributeError:
    pass #do nothing
try:
    CheckAccount(trialPD3)
except AttributeError:
    pass
try:
    CheckAccount(trialPD4)
except AttributeError:
    pass
try:
    CheckAccount(trialPD5)
except AttributeError:
    pass
#determine how to assign columns after find which columns are floats, int, has account names & a date

#determine Description Column, if not any of the other columns = description

def FindDescription(z):
    if z.name == 'Date':
    #trialPD1.name == 'Date':
        print('Date assigned.')
        return True
    else:
        pass
    if z.name == 'Account Name':
        print('Account Name assigned.')
        return True
    else:
        pass
    if z.name == 'Debit':
        print('Debit assigned.')
        return True
    else:
        pass
    if z.name == 'Credit':
        print('Credit assigned.')
        return True
    else:
        pass
    if z.name == 'Account #':
        print('Account # assigned.')
        return True
    else:
        print('Not assigned')
        z.name = 'Description'
    
while True:
    FindDescription(trialPD1)
    break
while True:
    FindDescription(trialPD2)
    break
while True:
    FindDescription(trialPD3)
    break
while True:
    FindDescription(trialPD4)
    break
while True:
    FindDescription(trialPD5)
    break
print(trialPD1.name)
print(trialPD2.name)
print(trialPD3.name)
print(trialPD4.name)
print(trialPD5.name)

#print(df.keys())
#-------------Review Debit and Credit, Debit isnt coming across------
df1 = [trialPD1, trialPD2, trialPD3, trialPD4, trialPD5]
df1 = pd.DataFrame(df1)
df1 = df1.T
df1 = df1[['Date', 'Description', 'Credit']]
print(df1.head(5))

