import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def renameNonConsecutiveWeeksAsDCategory(df,catname):
    df = df.rename(columns = {"NonConsecutiveWeeks":catname})
    return df


if __name__ == "__main__":
    df0 = pd.read_csv("../data/CA2020/ca2020D0.csv").set_index('County')
    df1 = pd.read_csv("../data/CA2020/ca2020D1.csv").set_index('County')
    df2 = pd.read_csv("../data/CA2020/ca2020D2.csv").set_index('County')
    df3 = pd.read_csv("../data/CA2020/ca2020D3.csv").set_index('County')
    df4 = pd.read_csv("../data/CA2020/ca2020D4.csv").set_index('County')

    df0 = df0.rename(columns = {"NonConsecutiveWeeks":"d0"})
    df1 = df1.rename(columns = {"NonConsecutiveWeeks":"d1"})
    df2 = df2.rename(columns = {"NonConsecutiveWeeks":"d2"})
    df3 = df3.rename(columns = {"NonConsecutiveWeeks":"d3"})
    df4 = df4.rename(columns = {"NonConsecutiveWeeks":"d4"})
    
    california2020 = pd.DataFrame(data={"FIPS":df0["FIPS"]})
    california2020['d4'] = df4['d4']
    california2020 = california2020.replace(np.nan,0)
    california2020['d3'] = df3['d3'] - california2020['d4']
    california2020 = california2020.replace(np.nan,0)
    california2020['d2'] = df2['d2'] - california2020['d3'] - california2020['d4']
    california2020 = california2020.replace(np.nan,0)
    california2020['d1'] = df1['d1'] - california2020['d2'] - california2020['d3'] - california2020['d4']
    california2020 = california2020.replace(np.nan,0)
    california2020['d0'] = df0['d0'] - california2020['d1']- california2020['d2'] - california2020['d3'] - california2020['d4']
    california2020 = california2020.replace(np.nan,0)

    consec0 = pd.read_csv("../data/CA2020/d0Consecutive.csv")
    consec1 = pd.read_csv("../data/CA2020/d1Consecutive.csv")
    consec2 = pd.read_csv("../data/CA2020/d2Consecutive.csv")
    consec3 = pd.read_csv("../data/CA2020/d3Consecutive.csv")
    consec4 = pd.read_csv("../data/CA2020/d4Consecutive.csv")

    consec0['DCat']=0
    consec1['DCat']=1
    consec2['DCat']=2
    consec3['DCat']=3
    consec4['DCat']=4
    consecCA2020 = pd.concat([consec0,consec1,consec2,consec3,consec4]).sort_values(by=["County","StartDate"])