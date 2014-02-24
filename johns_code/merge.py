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
#
#   basic plots
#
#
# TOA and RH
plt.scatter(TOA, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("TOA and RH")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/TOA_RH.png')
plt.clf()

# TOA and Tair
plt.scatter(TOA, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("TOA and Tair")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/TOA_Tair.png')
plt.clf()

# TOA and CC
plt.scatter(TOA, CC, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("TOA and CC")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("Cloud Cover (fraction)")
#plt.show()
plt.savefig('./plots/TOA_CC.png')
plt.clf()

# TOA and tau
plt.scatter(TOA, tau, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("TOA and Optical Depth")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("Optical depth")
#plt.show()
plt.savefig('./plots/TOA_tau.png')
plt.clf()

# TOA and Tr
TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
TOAMasked = [TOA[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
plt.scatter(TOAMasked, TrMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("TOA and Transmission")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("Transmission")
#plt.show()
plt.savefig('./plots/TOA_Tr.png')
plt.clf()

# SWin and RH
plt.scatter(SWin, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("SW in and RH")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/SW_RH.png')
plt.clf()

# SWin and Tair
plt.scatter(SWin, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("SW in and Tair")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/SW_Tair.png')
plt.clf()

# SWin and CC
plt.scatter(SWin, CC, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("SWin and CC")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Cloud Cover (fraction)")
#plt.show()
plt.savefig('./plots/SWin_CC.png')
plt.clf()

# SWin and tau
plt.scatter(SWin, tau, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("SWin and Optical Depth")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Optical depth")
#plt.show()
plt.savefig('./plots/SWin_tau.png')
plt.clf()

# SWin and Tr
TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
SWinMasked = [SWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
plt.scatter(SWinMasked, TrMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("SWin and Transmission")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Transmission")
#plt.show()
plt.savefig('./plots/SWin_Tr.png')
plt.clf()

# LWin and RH
plt.scatter(LWin, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("LW in and RH")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/LW_RH.png')
plt.clf()

# LWin and Tair
plt.scatter(LWin, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tair and LW in")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/LW_Tair.png')
plt.clf()

# LWin and CC
plt.scatter(LWin, CC, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("LWin and CC")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Cloud Cover (fraction)")
#plt.show()
plt.savefig('./plots/LWin_CC.png')
plt.clf()

# LWin and tau
plt.scatter(LWin, tau, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("LWin and Optical Depth")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Optical depth")
#plt.show()
plt.savefig('./plots/LWin_tau.png')
plt.clf()

# LWin and Tr
TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
LWinMasked = [LWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
plt.scatter(LWinMasked, TrMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("LWin and Transmission")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Transmission")
#plt.show()
plt.savefig('./plots/LWin_Tr.png')
plt.clf()

# Tr and RH
TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
RHMasked = [RH[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
plt.scatter(TrMasked, RHMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tr and RH")
plt.xlabel("Transmission")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/Tr_RH.png')
plt.clf()

# Tr and Tair
TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
TairMasked = [Tair[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
plt.scatter(TrMasked, TairMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tr and Tair")
plt.xlabel("Transmission")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/Tr_Tair.png')
plt.clf()

# Tr and CC
TrMasked = [Tr[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
CCMasked = [CC[x] for x in np.arange(0,len(LWin)) if not(np.isnan(Tr[x])) and (Tr[x]<=1.0)]
plt.scatter(TrMasked, CCMasked, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tr and CC")
plt.xlabel("Transmission")
plt.ylabel("Cloud Cover (fraction)")
#plt.show()
plt.savefig('./plots/Tr_CC.png')
plt.clf()

# tau and RH
plt.scatter(tau, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Optical Depth and RH")
plt.xlabel("Optical Depth")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/tau_RH.png')
plt.clf()

# tau and Tair
plt.scatter(tau, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Optical Depth and Tair")
plt.xlabel("Optical Depth")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/tau_Tair.png')
plt.clf()

# tau and CC
plt.scatter(tau, CC, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Optical Depth and CC")
plt.xlabel("Optical Depth")
plt.ylabel("Cloud Cover (fraction)")
#plt.show()
plt.savefig('./plots/tau_CC.png')
plt.clf()



TR = [TR[x] if not (np.isinf(TR[x])) else np.nan for x in np.arange(0,len(TR))]


# split data by cloud cover <0.4
clearLW = [LWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]<0.4)]
clearTair = [Tair[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]<0.4)]
cloudyLW = [LWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]>=0.4)]
cloudyTair = [Tair[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]>=0.4)]
clearSW = [SWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]<0.4)]
cloudySW = [SWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]>=0.4)]
clearSW = [SWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]<0.4)]
cloudySW = [SWin[x] for x in np.arange(0,len(LWin)) if not(np.isnan(CC[x])) and (CC[x]>=0.4)]



# Tair and LWin split for clear and cloudy
plt.scatter(clearLW, clearTair, color = (1,0.2,0), s=1, facecolor='0.1', alpha =0.4, lw = 1)
plt.scatter(cloudyLW, cloudyTair, color = (0,0.3,0.9), s=1, facecolor='0.1', alpha =0.4, lw = 1)
plt.title("Tair and LW in")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.legend(loc='best')
plt.show()
plt.savefig('./plots/LW_Tair.png')
plt.clf()

# Tair and SWin split for clear and cloudy
plt.scatter(clearSW, clearTair, color = (1,0.2,0), s=1, facecolor='0.1', alpha =0.4, lw = 1)
plt.scatter(cloudySW, cloudyTair, color = (0,0.3,0.9), s=1, facecolor='0.1', alpha =0.4, lw = 1)
plt.title("Tair and SW in")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.legend(loc='best')
plt.show()
plt.savefig('./plots/LW_Tair.png')
plt.clf()

