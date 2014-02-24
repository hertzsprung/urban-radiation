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

line = data.readline()

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
    
    line = data.readline()


data.close()


# time to decimal time
dday = []
for i in np.arange(len(time)) :
    t = time[i]
    (h, m, s) = t.split(':')
    result = (int(h) * 3600 + int(m) * 60 + int(s))/(24*60*60)
    dday.append(result)


#
# plots
#

# TOA and RH
plt.scatter(TOA, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("RH and TOA")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/TOA_RH.png')
plt.clf()

# TOA and Tair
plt.scatter(TOA, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tair and TOA")
plt.xlabel("TOA (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/TOA_Tair.png')
plt.clf()

# RH and SWin
plt.scatter(SWin, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("RH and SW in")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/SW_RH.png')
plt.clf()

# RH and LWin
plt.scatter(LWin, RH, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("RH and LW in")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("RH (%)")
#plt.show()
plt.savefig('./plots/LW_RH.png')
plt.clf()

# Tair and SWin
plt.scatter(SWin, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tair and SW in")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/SW_Tair.png')
plt.clf()

# Tair and LWin
plt.scatter(LWin, Tair, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Tair and LW in")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/LW_Tair.png')
plt.clf()

# rain and SWin
plt.scatter(SWin, rain, s=1, facecolor='0.1', alpha =0.4, lw = 0)
plt.title("Rain and SW in")
plt.xlabel("Shortwave in (Wm-2)")
plt.ylabel("Rain (mm)")
#plt.show()
plt.savefig('./plots/SW_rain.png')
plt.clf()

# rain and LWin
plt.scatter(LWin, rain, s=1, facecolor='2.1', alpha =0.4, lw = 0)
plt.title("Rain and LW in")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Rain (mm)")
#plt.show()
plt.savefig('./plots/LW_rain.png')
plt.clf()

# split day and night
dayLW = np.empty(len(LWin))
nightLW = np.empty(len(LWin))
dayLW[:] = np.nan
nightLW[:] = np.nan
DN2 = np.array(DN)
for i in DN :
    if DN[i] :
        dayLW[i] = LWin[i]
    else :
        nightLW[i] = LWin[i] 
        
dayLW = LWin[:]
nightLW = LWin[:]
dayTair = Tair[:]
nightTair = Tair[:]
i = 0
while i < len(LWin):
    if DN[i] == False:
        dayLW = dayLW[:i] + dayLW[i+1:]
        dayTair = dayTair[:i] + dayTair[i+1:]
    else:
        i += 1

while i < len(LWin):
    if DN[i] == True:
        nightLW = nightLW[:i] + nightLW[i+1:]
        nightTair = nightTair[:i] + nightTair[i+1:]
    else:
        i += 1

dayLW = [LWin[x] for x in np.arange(0,len(LWin)) if DN[x]]


# Tair and LWin
plt.scatter(dayLW, Tair, color = (1,0,0), s=1, facecolor='0.1', alpha =0.4, lw = 1, legend='Day')
plt.scatter(nightLW, Tair, color = (0,1,0), s=1, facecolor='0.1', alpha =0.4, lw = 1, label='Night')
plt.title("Tair and LW in")
plt.xlabel("Longwave in (Wm-2)")
plt.ylabel("Air Temperature (celcius)")
#plt.show()
plt.savefig('./plots/LW_Tair.png')
plt.clf()
