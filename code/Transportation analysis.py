import gmaps
import pandas as pd
import datetime
import time
import os
import numpy as np
import matplotlib.pyplot as plt
#readfile
#data = pd.read_csv("data0.csv")

time_format = '%Y/%m/%d %H:%M:%S'

pathFile = []
def isExistFileLabels():
    for x in os.listdir('F:/CaoHoc/Data engineer/Geolife Trajectories 1.3/Geolife Trajectories 1.3/Data'):
        for y in os.listdir('F:/CaoHoc/Data engineer/Geolife Trajectories 1.3/Geolife Trajectories 1.3/Data/'+x):
            if(y.endswith('.txt')):
                pathFile.append('F:/CaoHoc/Data engineer/Geolife Trajectories 1.3/Geolife Trajectories 1.3/Data/'+x)

def getTimeIntervalOfPoints(pi, pj):
    t_i = time.mktime(time.strptime(pi, time_format))
    t_j = time.mktime(time.strptime(pj, time_format))
    return t_j - t_i
isExistFileLabels()
def convertToCsvFile():
    for i in range(len(pathFile)):
            f = pd.read_csv(pathFile[i]+'/labels.txt',delimiter = '\t')
            f.to_csv(pathFile[i]+'/labels.csv',index=None)
totalResult = {}
def calculateDuration():
    for j in range(len(pathFile)):
        dataLabels = pd.read_csv(pathFile[j]+'/labels.csv')
        start = dataLabels.iloc[:,0].values.tolist()
        end = dataLabels.iloc[:,1].values.tolist()
        vehicle = dataLabels.iloc[:,2].values.tolist()
        result = {}
        for i in range(len(vehicle)):
            result[vehicle[i]] = 0;
        for i in range(len(start)):
            duration = getTimeIntervalOfPoints(start[i],end[i])
            result[vehicle[i]] +=  duration
        totalResult[pathFile[j]] = result

convertToCsvFile()
calculateDuration()
table = pd.DataFrame.from_dict(totalResult)
table = table.fillna(0)



table["total"] = table.sum(axis=1)
table = table.transpose()
color = ('red','coral','darkorange','olive','lawngreen','palegreen','turquoise','cyan','lavender','indigo','violet')
table.to_csv('result.csv',index = None)
plt.figure(figsize=(10,5))
plt.bar(table.columns.values,table.iloc[-1],color = color)
plt.title('time of using different transportation')
plt.xlabel('Transpotation mode')
plt.ylabel('Time')
plt.show()