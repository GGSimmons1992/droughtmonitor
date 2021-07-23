import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from datetime import datetime

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

def plotConsecTimeSeries(df,countyName,legendLoc):
    fig,ax = plt.subplots()
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
    xlims = [datetime.strptime('2020-01-01','%Y-%m-%d').date(),datetime.strptime('2020-12-31','%Y-%m-%d').date()]
    ax.set_xlim(xlims)
    handles, labels = ax.get_legend_handles_labels()
    handle_list, label_list = [], []
    for handle, label in zip(handles, labels):
        if label not in label_list:
            handle_list.append(handle)
            label_list.append(label)
    ax.legend(handle_list, label_list,loc=legendLoc)
    plt.tight_layout()
    plt.savefig(f'../images/{countyName}.png')
    plt.show()

def bootstrap_means(arr):
    data = np.array(arr)
    sampleMeans = []
    for row in range(10000):
        bootstrappedSample = np.array([np.random.choice(data) for _ in range(len(data))])
        sampleMeans.append(bootstrappedSample.mean())
    meanOfSamples = np.mean(sampleMeans)
    lowerCI,upperCI = np.percentile(sampleMeans,[2.5,97.5])
    return sampleMeans,meanOfSamples,lowerCI,upperCI

def plotBootstrapSamples(countyName,sampleMeans,meanOfSamples,lowerCI,upperCI):
    fig,ax = plt.subplots()
    bars = ax.hist(sampleMeans,bins=100)
    barheight = np.max(bars[0])
    ax.plot([lowerCI,lowerCI],[0,barheight])
    ax.plot([meanOfSamples,meanOfSamples],[0,barheight])
    ax.plot([upperCI,upperCI],[0,barheight])
    ax.set_xlabel('average category')
    ax.set_title(f'{countyName} avg category = {round(meanOfSamples,2)} ([{round(lowerCI,2)},{round(upperCI,2)}])')
    plt.tight_layout()
    plt.savefig(f'../images/{countyName}95percentCI.png',)
    plt.show()