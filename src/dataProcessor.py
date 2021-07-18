import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def defineColor(dcat):
    if (dcat == 0):
        return 'yellow'
    if (dcat == 1):
        return 'orange'
    if (dcat == 2):
        return 'red'
    if (dcat == 3):
        return 'brown'
    if (dcat == 4):
        return 'black'

def plotConsecTimeSeries(ax,df,countyName,legendLoc):
    for index, row in df.iterrows():
        x=[row['StartDate'],row['EndDate']]
        y=[row['DCat'],row['DCat']]
        c=defineColor(row['DCat'])
        ax.fill_between(x,-1,y,color=c,label=f'D{row["DCat"]}')
    ax.set_title(f'{countyName} drought status 2020')
    ax.set_xlabel('date')
    ax.tick_params(axis='x',labelrotation=45)
    ax.set_ylabel('drought category')
    ax.set_ylim([-1,4])
    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    ax.legend(handle_list, label_list,loc=legendLoc)
    plt.show()
    plt.savefig(f'../images/{countyName}.png')

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