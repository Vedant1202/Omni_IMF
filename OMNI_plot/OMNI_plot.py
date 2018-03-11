
import matplotlib.pyplot as plt
import pandas as pd

def dicti():
    D = {1: 'HI_Lat', 2: 'HI_Long', 3: 'BR RTN', 4: 'BT RTN', 5: 'BN RTN', 6:'FMagAvg|B|', 7:'BF_speed', 8:'THETA', 9:'PHI', 10:'ION', 11:'Temp'}
    return D

def in_index():
    ## create an index
    dic = dicti()
    a = input()
    b = dic.get(a)
    return b

def datafr():
    ## read dataframe
    df = pd.read_table("OMNI32.txt", sep='\t', header=None)
    df.columns = ["Sequence"]
    df = pd.DataFrame(df.Sequence.str.split('  ',13).tolist(),
                                      columns = ["Year", "A", "B", "HI_Lat", "HI_Long", "BR RTN", "BT RTN", "BN RTN", "FMagAvg|B|", "BF_speed", "THETA", "PHI", "ION", "Temp"])

    df["Year"] = df["Year"].map(str)+str("/")+df["A"]+str("/")+df["B"]
    del df["A"]
    del df["B"]
    del df["Year"]
    return df

def plot_dat(A):
    ## plot data
    print("\n\n")
    d = in_index()
    plt.plot(A, label = d)
    plt.legend()
    plt.show()

def main():
    df2 = pd.read_table("ref2.txt", sep='\t')
    print(df2)
    c = in_index()
    df = datafr()
    df = df.head()
    plot_dat(df)

main()




