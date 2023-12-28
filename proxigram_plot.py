#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:21:54 2022

@author: bart924
"""

#This is to create a proxigram graph






import pandas as pd # for reading csv's and creating the dataframe
import matplotlib.pyplot as plt #for plotting
import os #for changing the directory
import mpl_toolkits.axisartist as axisartist
import numpy as np
import matplotlib.transforms
import matplotlib

plt.rcParams["font.family"] = "Arial"

howmanyplots = 1 #numberofplotsyou want
currentdirectory = "/Volumes/BESECProjectArun/Experimental_results/APT/H_study/Deuterium/D_conc_distribution/PureFe"
csvfilename1 = "R31_19280-v02_1D_conc.csv"


os.chdir(currentdirectory)
savefilename = "R31_19280-v02_1D_conc" #defaults with .png extension.

resolution = 1200 # resolution for the saved figure in dots per inch. 1200 is usually good.
lowresolution = 150 # resolution for ppt slides


df1 = pd.read_csv(csvfilename1)

#List the x range that you would like to plot
xminrange = 0
xmaxrange = 30
#Officially, plot only normalized plots. In this code it is against the highest peak (Highest peak is "1" and the rest is a fraction of that)
yminrange = 90 # Low enough to see the background floor but not waste space
ymaxrange = 100 #1.1 for the tiny bit of space up top. 

yminrangesmall = 0
ymaxrangesmall = 0.5

df1.rename(index=str,columns={"Distance (nm)":"Distance"},inplace=True)
df1["Distance"] = df1["Distance"] - xminrange
df1 = df1[df1.Distance <= xmaxrange]

fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True)

plotFe = df1.plot("Distance", "Fe %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(1,0,1)], label = "Fe", legend = False,fontsize=20,yerr="Fe % Sigma")
# plotCr = df1.plot("Distance", "Cr %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(0,0,1)], label = "Cr", legend = False,fontsize=20)
# plotNi = df1.plot("Distance", "Ni %", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(0,204/255,0)], label = "Ni", legend = False,fontsize=20)
plotHone = df1.plot("Distance", "H %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(102/255,102/255,0)], label = "H", legend = False,fontsize=20,yerr="H % Sigma")
plotHtwo = df1.plot("Distance", "He %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(255/255,0,0)], label = "$^{2}$H", legend = False,fontsize=20,yerr="He % Sigma")
plotO = df1.plot("Distance", "O %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(0,0,1)], label = "O", legend = False,fontsize=20,yerr="O % Sigma")


# handles, labels = ax1.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center')

# fig.legend(handles=[plotFe,plotCr,plotHone])
# bbox_to_anchor=(0., 2.02, 1., .202), loc=0,
#  ncol=5, mode="expand", borderaxespad=0.)

fig.text(0.02, 0.48, 'Concentration [at. %]', ha='center', va='center', rotation='vertical',fontsize=20)
plt.subplots_adjust(hspace=0.17)
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

# os.chdir(currentdirectory)
# fig.savefig(savefilename, dpi = resolution, bbox_inches='tight')
# savefilenamelowres = savefilename + "_lowres"
# fig.savefig(savefilenamelowres, dpi = lowresolution, bbox_inches='tight')