# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:52:20 2023

@author: bart924
"""

#Peak Decomposition. This version focuses around Fe, Ni, Cr and oxides
#We ignore N, and C.

import pandas as pd # for reading csv's and creating the dataframe
import os #for changing the 
import matplotlib as plt
import matplotlib.transforms

currentdirectory = os.chdir(os.getcwd()) # Save the code in the same folder as the data
resolution = 1200
lowresolution = 300
savefilename = "asdf"
csvfilename1 = ""
csvmass = "csvmass.csv"


df1 = pd.read_csv(csvfilename1)
dfmass = pd.read_csv(csvmass)

FeHplus2tot = df1["27p5 %"] / (dfmass["Fe55"]*dfmass["H1"])

Feplus2tot = ((df1["28 %"]-(dfmass["Fe55"]*dfmass["H2"]*FeHplus2tot))/dfmass["Fe56"]+(df1["28p5 %"]-(dfmass["Fe56"]*dfmass["H1"]*FeHplus2tot))/dfmass["Fe57"])/2

Crplus2tot = (df1["25 %"]/dfmass["Cr50"]+df1["26 %"]/dfmass["Cr52"]+df1["26p5 %"]/dfmass["Cr53"]+(df1["27 %"]-(dfmass["Fe54"]*Feplus2tot)/dfmass["Cr54"]))/4

NiHplus2totchunk1 = (df1["29p5 %"]-(dfmass["Fe58"]*dfmass["H1"]*Feplus2tot))/(dfmass["Ni58"]*dfmass["H1"])
NiHplus2totchunk2 = dfmass["31p5"]/(dfmass["Ni62"]*dfmass["H1"])
NiHplus2totchunk3 = dfmass["32p5"]/(dfmass["Ni64"]*dfmass["H1"])
NiHplus2tot = (NiHplus2totchunk1+NiHplus2totchunk2+NiHplus2totchunk3)/3

Niplus2totchunk1 = (df1["29 %"]-(df1["Fe58"]*Feplus2tot+dfmass["Fe57"]*dfmass["H1"]*FeHplus2tot))/dfmass["Ni58"]
Niplus2totchunk2 = (df1["30 %"]-(dfmass["Ni58"]*dfmass["H2"])*NiHplus2tot)/dfmass["Ni60"]
Niplus2totchunk3 = (df1["30p5 %"]-(dfmass["Ni60"]*dfmass["H1"]*NiHplus2tot))/dfmass["Ni61"]
Niplus2totchunk4 = (df1["31 %"]-(dfmass["Ni60"]*dfmass["H2"]+dfmass["Ni61"]*dfmass["H1"])*NiHplus2tot)/dfmass["Ni62"]
Niplus2tot = (Niplus2totchunk1+Niplus2totchunk2+Niplus2totchunk3+Niplus2totchunk4)/4

O2plus1tot = (df1["32 %"]-dfmass["Ni64"]*Niplus2tot)/(dfmass["O16"]*dfmass["O16"]) 

FeOplus2chunk1 = (df1["36 %"]-dfmass["O18"]^2*O2plus1tot)/(dfmass["Fe54"]*dfmass["O18"]+dfmass["Fe56"]*dfmass["O16"])
FeOplus2chunk2 = df1["36p5 %"]/(dfmass["Fe56"]*dfmass["O17"]+dfmass["Fe57"]*dfmass["O16"])
FeOplus2tot = FeOplus2chunk1+FeOplus2chunk2

CrOplus2chunk1 = (df1["33 %"]-(dfmass["16"]*dfmass["O17"]*O2plus1tot))/(dfmass["Cr50"]*dfmass["O16"])
CrOplus2chunk2 = (df1["34 %"]-dfmass["16"]*dfmass["O18"]*O2plus1tot)/(dfmass["Cr52"]*dfmass["O16"]+dfmass["Cr50"]*dfmass["O18"])
CrOplus2chunk3 = df1["34p5 %"]/(dfmass["Cr53"]*dfmass["O16"]+dfmass["Cr52"]*dfmass["O17"])                 
CrOplus2tot = (CrOplus2chunk1 + CrOplus2chunk2 + CrOplus2chunk3)/3

NiOplus2start = (df1["37 %"]-(dfmass["Fe56"]*dfmass["O18"]+dfmass["Fe58"]*dfmass["O16"])*FeOplus2tot)/(dfmass["Ni58"]*dfmass["O16"])

NiOHplus2chunk1 = (df1["37p5 %"]-(dfmass["58"]*dfmass["O17"]*NiOplus2start+dfmass["Fe58"]*dfmass["O17"]*FeOplus2tot))/(dfmass["Ni58"]*dfmass["O17"]*dfmass["H1"]+dfmass["Ni58"]*dfmass["O16"]*dfmass["H2"])
NiOHplus2chunk2 = (df1["38p5 %"]-(dfmass["Ni61"]*dfmass["O16"]*dfmass["Ni60"]*dfmass["O17"])*NiOplus2start)/(dfmass["Ni60"]*dfmass["O16"]*dfmass["H1"]+dfmass["Ni58"]*dfmass["O17"]*dfmass["H2"])
NiOHplus2chunk3top = df1["39p5 %"]-(dfmass["Ni62"]*dfmass["O17"]+dfmass["Ni61"]*dfmass["O18"])*NiOplus2start
NiOHplus2chunk3bot = dfmass["Ni62"]*dfmass["O16"]*dfmass["H1"]+dfmass["Ni61"]*dfmass["O17"]*dfmass["H1"]+dfmass["Ni60"]*dfmass["Ni61"]*dfmass["O16"]*dfmass["H2"]+dfmass["Ni60"]*dfmass["O17"]*dfmass["H2"]
NiOHplus2chunk3 = NiOHplus2chunk3top/NiOHplus2chunk3bot
NiOHplus2chunk4 = (df1["40p5 %"]-(dfmass["Ni64"]*dfmass["O17"]*NiOplus2start))/(dfmass["Ni64"]*dfmass["O16"]*dfmass["H1"]+dfmass["Ni62"]*dfmass["O17"]*dfmass["H2"]+dfmass["Ni62"]*dfmass["O18"]*dfmass["H1"])  
NiOHplus2tot = (NiOHplus2chunk1+NiOHplus2chunk2+NiOHplus2chunk3+NiOHplus2chunk4)/4

NiOplus2totchunk1top = df1["38 %"]-(dfmass["Ni58"]*dfmass["O16"]*dfmass["H2"]+dfmass["Ni58"]*dfmass["O17"]*dfmass["H1"])*NiOHplus2tot
NiOplus2totchunk1bot = dfmass["Ni60"]*dfmass["O16"]+dfmass["Ni58"]+dfmass["O18"]
NiOplus2totchunk1 = NiOplus2totchunk1top / NiOplus2totchunk1bot
NiOplus2totchunk2top = df1["39 %"]-(dfmass["Ni60"]*dfmass["O17"]*dfmass["H1"]+dfmass["Ni60"]*dfmass["O16"]*dfmass["H2"]+dfmass["Ni61"]*dfmass["O16"]*dfmass["H1"])*NiOHplus2tot
NiOplus2totchunk2bot = dfmass["Ni60"]*dfmass["O18"]*dfmass["Ni61"]*dfmass["O17"]+dfmass["Ni62"]*dfmass["O16"]
NiOplus2totchunk2 = NiOplus2totchunk2top/NiOplus2totchunk2bot
NiOplus2totchunk3top = df1["40 %"]-(dfmass["Ni60"]*dfmass["O18"]*dfmass["H2"]+dfmass["Ni61"]*dfmass["O17"]*dfmass["H2"]+dfmass["Ni61"]*dfmass["O18"]*dfmass["H1"]+dfmass["Ni62"]*dfmass["O16"]*dfmass["H2"]+dfmass["Ni62"]*dfmass["O17"]*dfmass["H1"])*NiOHplus2tot
NiOplus2totchunk3bot = dfmass["Ni60"]*dfmass["O16"]*dfmass["H1"]+dfmass["Ni58"]*dfmass["O17"]*dfmass["H2"]
NiOplus2totchunk3 = NiOplus2totchunk3top/NiOplus2totchunk3bot
#Note the 4th chunk is NiOplus2start. It is not redefined, but we include it and divide by 4.
NiOplus2tot = (NiOplus2start+NiOplus2totchunk1+NiOplus2totchunk2+NiOplus2totchunk3)/4


Fe1plustot = (df1["56 %"]/dfmass["Fe56"] + df1["57 %"]/dfmass["Fe57"])/2
Cr1plustot = (df1["50 %"]/dfmass["Cr50"] + df1["52 %"]/dfmass["Cr52"] + df1["53 %"]/dfmass["Cr53"] + (df1["54 %"]-(dfmass["Fe54"]*Feplus2tot)/dfmass["Cr54"]))/4
Ni1plustot = ((df1["58 %"]-dfmass["Fe58"]*Feplus2tot)/dfmass["Ni58"] + df1["60 %"]/dfmass["Ni60"] + df1["61 %"]/dfmass["Ni61"] + df1["62 %"]/dfmass["Ni62"])/4


df1["Fe %"] = df1["Fe %"] + FeHplus2tot / 2 + Feplus2tot + FeOplus2tot / 2 + Fe1plustot
df1["Cr %"] = df1["Cr %"] + Crplus2tot + CrOplus2tot / 2 + Cr1plustot
df1["Ni %"] = df1["Ni %"] + NiHplus2tot / 2 + Niplus2tot + NiOplus2tot / 2 + NiOHplus2tot / 3 + Ni1plustot
df1["O %"] = df1["O %"] + O2plus1tot * 2 + FeOplus2tot / 2 + CrOplus2tot / 2 + NiOHplus2tot / 3

Fecounts = df1["Fe %"] * df1["Ion Count"]
Crcounts = df1["Cr %"] * df1["Ion Count"]
Nicounts = df1["Ni %"] * df1["Ion Count"]
Ocounts = df1["O %"] * df1["Ion Count"]

allcounts = Fecounts + Crcounts + Nicounts + Ocounts

df1["Fe %"] = Fecounts / allcounts
df1["Cr %"] = Crcounts / allcounts
df1["Ni %"] = Nicounts / allcounts
df1["O %"] = Ocounts / allcounts


#List the x range that you would like to plot
xminrange = 1
xmaxrange = 15
#Officially, plot only normalized plots. In this code it is against the highest peak (Highest peak is "1" and the rest is a fraction of that)
yminrange = 1 # Low enough to see the background floor but not waste space
ymaxrange = 70 #1.1 for the tiny bit of space up top. 

yminrangesmall = 0
ymaxrangesmall = 2.3

df1.rename(index=str,columns={"Distance (nm)":"Distance"},inplace=True)
df1["Distance"] = df1["Distance"] - xminrange
df1 = df1[df1.Distance <= xmaxrange]

fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True, gridspec_kw={'height_ratios': [3, 1.5]})

plotFe = df1.plot("Distance", "Fe %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(1,0,1)], label = "Fe", legend = False,fontsize=20,yerr="Fe % Sigma")
plotCr = df1.plot("Distance", "Cr %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(0,0,1)], label = "Cr", legend = False,fontsize=20,yerr="Cr % Sigma")
plotNi = df1.plot("Distance", "Ni %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(0,204/255,0)], label = "Ni", legend = False,fontsize=20,yerr="Ni % Sigma")
plotO = df1.plot("Distance", "O %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(173/255,216/255,230/255)], label = "O", legend = False,fontsize=20,yerr="O % Sigma")


# plotHone = df1.plot("Distance", "H %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(102/255,102/255,0)], label = "H", legend = False,fontsize=20,yerr="H % Sigma")
# plotHtwo = df1.plot("Distance", "He %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(255/255,0,0)], label = "$^{2}$H", legend = False,fontsize=20,yerr="He % Sigma")

# handles, labels = ax1.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center')

# fig.legend(handles=[plotFe,plotCr,plotHone])
# bbox_to_anchor=(0., 2.02, 1., .202), loc=0,
#  ncol=5, mode="expand", borderaxespad=0.)

fig.text(0.02, 0.48, 'Concentration [at. %]', ha='center', va='center', rotation='vertical',fontsize=20)
plt.subplots_adjust(hspace=0.05,top=0.9, bottom = 0.1)
plt.xlabel("Distance [nm]", fontsize=20)

ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

os.chdir(currentdirectory)
fig.savefig(savefilename, dpi = resolution, bbox_inches='tight')
savefilenamelowres = savefilename + "_lowres"
fig.savefig(savefilenamelowres, dpi = lowresolution, bbox_inches='tight')

