#import os
#os.chdir('G:\\team project\\python')
#del os

import numpy as np
import matplotlib.pyplot as plt

data = open('data/London_MET_20102012.csv')

header = data.readline()     # "TIME","day","TOA","SWin","LWin","Tair","RH","rain"
units = data.readline()

time = []
day = []
DN = []
TOA = []
SWin = []
LWin = []
Tair =[]
RH = []
rain = []
Tr = []

line = data.readline()
i = 0

while len(line.split())==9 :
    lineSplit = line.split()
    time.append( lineSplit[1])        # time and day headers are wrong way round in file
    day.append( lineSplit[0])
    if lineSplit[2]!='TRUE' : DN.append( True)
    else : DN.append( False)
    if lineSplit[3]!='NA' : TOA.append( float(lineSplit[3]))
    else : TOA.append( np.nan)
    if lineSplit[4]!='NA' :SWin.append( float(lineSplit[4]))
    else : SWin.append( np.nan)
    if lineSplit[5]!='NA' :LWin.append( float(lineSplit[5]))
    else : LWin.append( np.nan)
    if lineSplit[6]!='NA' :Tair.append( float(lineSplit[6]))
    else : Tair.append( np.nan)
    if lineSplit[7]!='NA' :RH.append( float(lineSplit[7]))
    else : RH.append( np.nan)
    if lineSplit[8]!='NA' :rain.append( float(lineSplit[8]))
    else : rain.append( np.nan)
    if TOA[i] != 0.0 : Tr.append(SWin[i]/TOA[i])
    else : Tr.append(np.nan)
    
    line = data.readline()
    i = i+1

data.close()

data = open('data/model_obs.dat')

header = data.readline()     # "#timestamp, TOA, SWin, LWin, mTOA, tau, mSW, mLW, RH, rain, CC"
units = data.readline()

time2 = []   # 0
day2 = []    # 1
#DN = []    
TOA2 = []    # 2
SWin2 = []   # 3
LWin2 = []   # 4
mTOA2 = []   # 5
tau2 = []    # 6
mSW2 = []    # 7
mLW2 = []    # 8
RH2 = []     # 9
rain2 = []   # 10
CC2 = []     # 11

line = data.readline()

while len(line.split())== 2 :
    lSplit = line.split()
    lineSplit = [lSplit[0]] + lSplit[1].split(',')
    day2.append( lineSplit[0])
    time2.append( lineSplit[1])        # time and day headers are wrong way round in file
    
    if lineSplit[2]!='NA' : TOA2.append( float(lineSplit[2]))
    else : TOA2.append( np.nan)
    if lineSplit[3]!='NA' :SWin2.append( float(lineSplit[3]))
    else : SWin2.append( np.nan)
    if lineSplit[4]!='NA' :LWin2.append( float(lineSplit[4]))
    else : LWin2.append( np.nan)
    if lineSplit[5]!='NA' : mTOA2.append( float(lineSplit[5]))
    else : mTOA2.append( np.nan)
    if lineSplit[6]!='NA' : tau2.append( float(lineSplit[6]))
    else : tau2.append(np.nan)
    if lineSplit[7]!='NA' : mSW2.append( float(lineSplit[7]))
    else : mSW2.append( np.nan)
    if lineSplit[8]!='NA' :mLW2.append( float(lineSplit[8]))
    else : mLW2.append( np.nan)
    if lineSplit[9]!='NA' :RH2.append( float(lineSplit[9]))
    else : RH2.append( np.nan)
    if lineSplit[10]!='NA' :rain2.append( float(lineSplit[10]))
    else : rain2.append( np.nan)
    if lineSplit[11]!='NA' :CC2.append( float(lineSplit[11]))
    else : CC2.append( np.nan)
   
    line = data.readline()

data.close()

lenfile1 = len(time)
lenfile2 = len(time2)
indDict = {}

mTOA = []   # 5
tau = []    # 6
mSW = []    # 7
mLW = []    # 8
CC = []     # 11

if lenfile1 >= lenfile2 :
    for i in np.arange(lenfile2) :
        indDict[(day2[i],time2[i])] = i
    for i in np.arange(lenfile1) :
        if indDict.has_key((day[i],time[i])) :
            mTOA.append (mTOA2[indDict[(day[i],time[i])]])
            tau.append (tau2[indDict[(day[i],time[i])]])
            mSW.append (mSW2[indDict[(day[i],time[i])]])
            mLW.append (mLW2[indDict[(day[i],time[i])]])
            CC.append (CC2[indDict[(day[i],time[i])]])
        else :
            mTOA.append (np.nan)
            tau.append (np.nan)
            mSW.append (np.nan)
            mLW.append (np.nan)
            CC.append (np.nan)

#

data = open('data/London_CL31_totalBSC_50m15min_OctDec.csv')

header = data.readline()     # 

time3 = []
day3 = []
levels = []
profile = []
mean = []
column = []
nlevels = len(header.split(','))-1

for i in np.arange(nlevels) :
    levels.append([])

i=0
line = data.readline()
while len(line.split())>1 :
    lSplit = line.split()
    lineSplit = [lSplit[0]] + lSplit[1].split(',')
    day3.append( lineSplit[0])
    time3.append( lineSplit[1])        # time and day headers are wrong way round in file
    colsum = 0.0
    profile.append(lineSplit[2:nlevels])
    # for j in np.arange(nlevels) :
        # if lineSplit[j+2]!='NA' : 
            # levels[i].append( float(lineSplit[j+2]))
            # colsum = colsum + float(lineSplit[j+2])
            # column.append(colsum)
        # else : levels[i].append( np.nan)
    # i =i+1
    line = data.readline()

data.close()

# replace NA with np.nan
for i in profile :
    for j in np.arange(nlevels-2) :
        if i[j] == 'NA' :
            i[j] = np.nan
        else : i[j] = float(i[j])


km = [[],[],[],[],[],[],[]]
for i in profile :
    kmsum = 0
    for j in np.arange(0,20):
        kmsum = kmsum + i[j]
    km[0].append(kmsum/20.0)
    kmsum = 0
    for j in np.arange(20,40):
        kmsum = kmsum + i[j]
    km[1].append(kmsum/20.0)
    kmsum = 0
    for j in np.arange(40,60):
        kmsum = kmsum + i[j]
    km[2].append(kmsum/20.0)
    kmsum = 0
    for j in np.arange(60,80):
        kmsum = kmsum + i[j]
    km[3].append(kmsum/20.0)
    kmsum = 0
    for j in np.arange(80,100):
        kmsum = kmsum + i[j]
    km[4].append(kmsum/20.0)
    kmsum = 0
    for j in np.arange(100,120):
        kmsum = kmsum + i[j]
    km[5].append(kmsum/20.0)
    kmsum = 0
    for j in np.arange(120,140):
        kmsum = kmsum + i[j]
    km[6].append(kmsum/20.0)

# merge
lenfile3 = len(time3)
indDict = {}

profmerge = []
kmmerge = [[],[],[],[],[],[],[]]

if lenfile1 >= lenfile3 :
    for i in np.arange(lenfile3) :
        indDict[(day3[i],time3[i])] = i
    for i in np.arange(lenfile1) :
        if indDict.has_key((day[i],time[i])) :
            kmmerge[0].append (km[0][indDict[(day[i],time[i])]])
            kmmerge[1].append (km[1][indDict[(day[i],time[i])]])
            kmmerge[2].append (km[2][indDict[(day[i],time[i])]])
            kmmerge[3].append (km[3][indDict[(day[i],time[i])]])
            kmmerge[4].append (km[4][indDict[(day[i],time[i])]])
            kmmerge[5].append (km[5][indDict[(day[i],time[i])]])
            kmmerge[6].append (km[6][indDict[(day[i],time[i])]])
            profmerge.append (profile[indDict[(day[i],time[i])]])
        else :
            kmmerge[0].append (np.nan)
            kmmerge[1].append (np.nan)
            kmmerge[2].append (np.nan)
            kmmerge[3].append (np.nan)
            kmmerge[4].append (np.nan)
            kmmerge[5].append (np.nan)
            kmmerge[6].append (np.nan)
            profmerge.append (np.nan)


####
#
#
# backscatter plots
#
#

for i in [0,1,2,3,4,5,6] :
    # BS and RH
    plt.scatter(kmmerge[i], RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
    plt.title("BS and RH between %i and %i km" %(i, i+1))
    plt.xlabel("Ceilometer Backscatter")
    plt.ylabel("RH (%)")
    #plt.show()
    plt.savefig('./plots/bs/BS%i_RH.png' %i)
    plt.clf()
    
    # BS and Tair
    plt.scatter(kmmerge[i], Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
    plt.title("BS and Tair between %i and %i km" %(i, i+1))
    plt.xlabel("Ceilometer Backscatter")
    plt.ylabel("Air Temperature (celcius)")
    #plt.show()
    plt.savefig('./plots/BS%i_Tair.png' %i)
    plt.clf()
    
    # BS and CC
    plt.scatter(kmmerge[i], CC, s=1, facecolor='0.1', alpha =0.4, lw = 0)
    plt.title("BS and CC between %i and %i km" %(i, i+1))
    plt.xlabel("Ceilometer Backscatter")
    plt.ylabel("Cloud Cover (fraction)")
    #plt.show()
    plt.savefig('./plots/BS%i_CC.png' %i)
    plt.clf()
    
    # BS and tau
    plt.scatter(kmmerge[i], tau, s=1, facecolor='0.1', alpha =0.4, lw = 0)
    plt.title("BS and Optical Depth between %i and %i km" %(i, i+1))
    plt.xlabel("Ceilometer Backscatter")
    plt.ylabel("Optical depth")
    #plt.show()
    plt.savefig('./plots/BS%i_tau.png' %i)
    plt.clf()
    
    # BS and Tr
    KMasked = [kmmerge[i][x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
    TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
    plt.scatter(KMasked, TrMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
    plt.title("BS and Tr between %i and %i km" %(i, i+1))
    plt.xlabel("Ceilometer Backscatter")
    plt.ylabel("Transmission")
    #plt.show()
    plt.savefig('./plots/BS%i_Tr.png' %i)
    plt.clf()




