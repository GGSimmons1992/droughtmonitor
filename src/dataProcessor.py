import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def renameNonConsecutiveWeeksAsDCategory(df,newName):
    df.rename({'NonConsecutiveWeeks':newName})
    return df

if __name__ == "__main__":
    df0 = pd.read_csv("../data/CA2020/ca2020D0.csv").set_index('County')
    df1 = pd.read_csv("../data/CA2020/ca2020D1.csv").set_index('County')
    df2 = pd.read_csv("../data/CA2020/ca2020D2.csv").set_index('County')
    df3 = pd.read_csv("../data/CA2020/ca2020D3.csv").set_index('County')
    df4 = pd.read_csv("../data/CA2020/ca2020D4.csv").set_index('County')

    #california2020 = pd.DataFrame(index=df0['County'])
    df0.head()