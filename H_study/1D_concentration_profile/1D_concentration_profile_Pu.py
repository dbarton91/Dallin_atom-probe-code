#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:57:59 2022

@author: bart924
"""

import pandas as pd  # for reading csv's and creating the dataframe
import matplotlib.pyplot as plt #for plotting
import os #for changing the directory
import mpl_toolkits.axisartist as axisartist
import numpy as np
import matplotlib.transforms
import matplotlib
import re
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
from matplotlib.font_manager import FontProperties
from matplotlib import rcParams

rcParams['xtick.labelsize'] = 12  # Change this to your desired font size
rcParams['ytick.labelsize'] = 12  # Change this to your desired font size
rcParams['xtick.major.width'] = 1.0
rcParams['xtick.minor.width'] = 1.0
rcParams['ytick.major.width'] = 1.0
rcParams['ytick.minor.width'] = 1.0
rcParams['xtick.major.size'] = 6.0
rcParams['xtick.minor.size'] = 4.0
rcParams['ytick.major.size'] = 6.0
rcParams['ytick.minor.size'] = 4.0
rcParams['xtick.major.pad'] = 6.0
rcParams['xtick.minor.pad'] = 6.0
rcParams['ytick.major.pad'] = 6.0
rcParams['ytick.minor.pad'] = 6.0
# rcParams['xtick.major.weight'] = 'bold'


plt.rcParams["font.family"] = "Arial"

howmanyplots = 1 #numberofplotsyou want
currentdirectory = r'C:\Users\bart924\Desktop'
csvfilename1 = "R5115_00738_tipprofile_01 - Cylinder ID 0 - 1D Concentration Profile - Z- axis.csv"


os.chdir(currentdirectory)
savefilename = "test7" #defaults with .png extension.

resolution = 1200 # resolution for the saved figure in dots per inch. 1200 is usually good.
lowresolution = 150 # resolution for ppt slides


df1 = pd.read_csv(csvfilename1)

#Remove the extras, multiply the percentages by the atoms, recalculate percentages, recalculate error

# Renaming columns with spaces and percentage signs
# List of words to remove


# Remove the incorrect header row
# df1 = df1.iloc[1:]

# Set the correct header using the next row
df1.columns = df1.iloc[0]

df1 = df1.iloc[1:]

# Reset the index after removing the first row
df1 = df1.reset_index(drop=True)

# typeincell= type(df1.at[0,0])
#
# print(typeincell)

words_to_remove = ["%", "atom", " ", "Atom", "(nm)"]



# Remove words from column names
for word in words_to_remove:
    df1.columns = [col.replace(word, '') for col in df1.columns]


# df1 = df1.dropna()

numeric_columns = ['Pu', 'Ga', 'O', 'Fe', 'Count', 'PuSigma', 'GaSigma', 'OSigma', 'FeSigma', 'Distance']
df1[numeric_columns] = df1[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)


df1["Pucounts"] = df1["Pu"] * df1["Count"] / 100
df1["Gacounts"] = df1["Ga"] * df1["Count"] / 100
df1["Ocounts"] = df1["O"] * df1["Count"] / 100
df1["Fecounts"] = df1["Fe"] * df1["Count"] / 100
df1["TotalCounts"] = df1["Pucounts"] + df1["Gacounts"] + df1["Ocounts"] + df1["Fecounts"]

df1["Pu"] = df1["Pucounts"] / df1["TotalCounts"] * 100
df1["Ga"] = df1["Gacounts"] / df1["TotalCounts"] * 100
df1["O"] = df1["Ocounts"] / df1["TotalCounts"] * 100
df1["Fe"] = df1["Fecounts"] / df1["TotalCounts"] * 100


#List the x range that you would like to plot
xminrange = 75
xmaxrange = 150
#Officially, plot only normalized plots. In this code it is against the highest peak (Highest peak is "1" and the rest is a fraction of that)
yminrange = 60 # Low enough to see the background floor but not waste space
ymaxrange = 90 #1.1 for the tiny bit of space up top.

yminrangesmall = 0.01
ymaxrangesmall = 15

# df1.rename(index=str,columns={"Distance (nm)":"Distance"},inplace=True)
df1["Distance"] = df1["Distance"] - xminrange
df1 = df1[df1.Distance <= xmaxrange]

# fig,(ax1) = plt.subplots()

fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True,gridspec_kw={'height_ratios': [2, 1]})

plotPu = df1.plot("Distance", "Pu", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax1, color = [(0,0,0)], label = "Pu", legend = False,fontsize=20)
plotGa = df1.plot("Distance", "Ga", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax2, color = [(232/255,119/255,34/255)], label = "Ga", legend = False,fontsize=20)
plotO = df1.plot("Distance", "O", xlim=[0,xmaxrange], ylim=[yminrange,ymaxrange], ax = ax2, color = [(108/255, 216/255, 255/255)], label = "O", legend = False,fontsize=20)
plotFe = df1.plot("Distance", "Fe", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(1,0,0)], label = "Fe", legend = False,fontsize=20)
# plotHtwo = df1.plot("Distance", "He %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(255/255,0,0)], label = "$^{2}$H", legend = False,fontsize=20,yerr="He % Sigma")
# plotO = df1.plot("Distance", "O %", xlim=[0,xmaxrange], ylim=[yminrangesmall,ymaxrangesmall], ax = ax2, color = [(0,0,1)], label = "O", legend = False,fontsize=20,yerr="O % Sigma")



# handles, labels = ax1.get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center')

# fig.legend(handles=[plotFe,plotCr,plotHone])
# bbox_to_anchor=(0., 2.02, 1., .202), loc=0,
#  ncol=5, mode="expand", borderaxespad=0.)

fig.text(0.02, 0.48, 'Concentration [at. %]', ha='center', va='center', rotation='vertical',fontsize=20, weight="bold")
plt.subplots_adjust(hspace=0.17)
plt.xlabel("Distance [nm]", fontsize=20, weight = 'bold')

ax1.fill_between(df1["Distance"],df1["Pu"]+df1["PuSigma"],df1["Pu"]-df1["PuSigma"], color = [(192/255,192/255,1)])
ax1.fill_between(df1["Distance"],df1["Ga"]+df1["GaSigma"],df1["Ga"]-df1["GaSigma"], color = [(1,192/255,1)])
ax1.fill_between(df1["Distance"],df1["O"]+df1["OSigma"],df1["O"]-df1["OSigma"], color = [(205/255,235/255,218/255)] )
ax2.fill_between(df1["Distance"],df1["Fe"]+df1["FeSigma"],df1["Fe"]-df1["FeSigma"], color = [(255/255,205/255,205/255)] )


ax1.tick_params(axis="x", bottom=False, top=True, labelbottom=False, labeltop=False, direction="in")
ax1.tick_params(axis="y", left=True, right=True, labelleft=True, labelright=False, direction="in")
ax2.tick_params(axis="x", bottom=True, top=False, labelbottom=True, labeltop=False, direction="in")
ax2.tick_params(axis="y", left=True, right=True, labelleft=True, labelright=False, direction="in")

# fontprops = FontProperties(weight='bold')

# ax1.set_xticklabels(ax1.get_xticks(), fontproperties=fontprops)
# ax1.set_yticklabels(ax1.get_yticks(), fontproperties=fontprops)

# ax2.set_xticklabels(ax2.get_xticks(), fontproperties=fontprops)
# ax2.set_yticklabels(ax2.get_yticks(), fontproperties=fontprops)



# ax2.xaxis.set_minor_locator(MultipleLocator(2.5))

# ax1.tick_params(which='both', width=2)
# ax2.tick_params(which='minor')



ax1.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)

# ax2.xaxis.tick_bottom()

d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)


ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)

fig.savefig(savefilename, dpi = resolution, bbox_inches='tight')
savefilenamelowres = savefilename + "_lowres"
fig.savefig(savefilenamelowres, dpi = lowresolution, bbox_inches='tight')