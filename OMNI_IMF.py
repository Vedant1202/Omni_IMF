## IMF dataframe monitor

import pandas as pd


def listing():
    ##Takes the input and advances to print the respective data.
    print("Enter Day(ranging from 1-365) and Hour(ranging from 0-23)")
    k,l = input().split()
    k = int(k)
    l = int(l)
    n = (k-1)*24 + l
    return n

##df.OMNI_DATA = df.OMNI_DATA.astype(float).fillna(0.0)
def set_input():
    pd.set_option('display.height', 1000)
    pd.set_option('display.max_rows', 8762)
    pd.set_option('display.max_columns', 1000)
    pd.set_option('display.width', 2000)

def allData():
    ##Prints all available data.
    df = pd.read_table("OMNI31.txt", sep='\t', header=0)
    ref = pd.read_table("reference.txt", sep='\t', header = None)
    ref.columns = ["Reference Table for Reading Data"]
    print(ref)
    
    set_input()
    print("\n \n \t \t OMNI IMF Data is:")
    print("\n", df)



def main():
    df = pd.read_table("OMNI31.txt", sep='\t', header=None)
    ref = pd.read_table("reference.txt", sep='\t', header = None)
    ref.columns = ["Reference Table for Reading Data"]
   
    
    n = listing()
    print(ref)
    print("\n \n \t \t OMNI IMF Data is:")
    L = list()
    L = [df.ix[n]]
    set_input()
    print("\n", L)
    
print("Enter 'full_data for entire data frame and 'specific_data' for specific frame'.")
inp = input()
if inp == "full_data":
    allData()
elif inp == "specific_data":
    main()
else:
    print("Invalid Input.")


   

