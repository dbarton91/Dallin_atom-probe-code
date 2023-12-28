#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:14:11 2022

@author: bart924
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import os

currentdirectory = "/Volumes/BESECProjectArun/Experimental_results/APT/H_study/H_DR_PR_parameterstudy/Concentrations"
resolution = 1200 # resolution for the saved figure in dots per inch. 1200 is usually good.
lowresolution = 300 # resolution for ppt slides

savefilename = "official3" #defaults with .png extension.

arialfont = {'fontname':'Arial'}


markersize = 125
labelsizey = 20
labelsizex = 20

#Pure Fe Data
X1 = (0.5,0.5,0.5)
X2 = (1.0,1.0,1.0)
X3 = (3.0,3.0,3.0)
Y = (50.,125.,200.)
Z1 = (4.07,1.29,0.805)
Z2 = (1.89,0.63,0.41)
Z3 = (0.55,0.21,0.13)

#Fe18Cr10Ni
Y1W16 = (50.,200.) #DR 0.5
Y2W16 = (50.,125.,200.) #DR 3
Z1W16 = (3.61,0.98)  #DR 0.5
Z2W16 = (0.39,0.30,0.41) #DR 3

#Fe18Cr14Ni
Y1W26 = (50.,200.) #DR 0.5
Y3W26 = (50., 200.) #DR 3.0
Z1W26 = (3.24,1.03) 
Z3W26 = (0.63,0.38)

fig, axes = plt.subplots(nrows=1,ncols=3,figsize=(9.75,3.25), sharey='row')
axes = axes.flatten()
plt.rcParams["font.family"] = "Arial"


axes[0].scatter(Y,Z1,marker='o',color='k',s=markersize)
axes[0].scatter(Y,Z2,marker='s',color='k',s=markersize)
axes[0].scatter(Y,Z3,marker='*',color='k',s=markersize)
axes[0].legend(['DR = 0.5%','DR = 3.0%'], fontsize = 12, frameon = True)

axes[1].scatter(Y1W16,Z1W16,marker='o',color='k',s=markersize)
axes[1].scatter(Y2W16,Z2W16,marker='*',color='k',s=markersize)
axes[1].legend(['DR = 0.5%','DR = 3.0%'], fontsize = 12, frameon = True)

axes[2].scatter(Y1W26,Z1W26,marker='o',color='k',s=markersize)
axes[2].scatter(Y3W26,Z3W26,marker='*',color='k',s=markersize)
axes[2].legend(['DR = 0.5%', 'DR = 3.0%'], fontsize = 12, frameon = True)

# axes.xaxis.set_major_locator(mpl.ticker.FixedLocator([1,2,3,4]))


mpl.rcParams['xtick.labelsize'] = labelsizex
mpl.rcParams['ytick.labelsize'] = labelsizey

xmajors = np.linspace(50, 200, 4)
xminors = np.linspace(50, 200, 13)
# thirds = np.linspace(50, 200, 50)
  
axes[0].xaxis.set_major_locator(mpl.ticker.FixedLocator(xmajors))
axes[0].xaxis.set_minor_locator(mpl.ticker.FixedLocator(xminors))
axes[1].xaxis.set_major_locator(mpl.ticker.FixedLocator(xmajors))
axes[1].xaxis.set_minor_locator(mpl.ticker.FixedLocator(xminors))
axes[2].xaxis.set_major_locator(mpl.ticker.FixedLocator(xmajors))
axes[2].xaxis.set_minor_locator(mpl.ticker.FixedLocator(xminors))

ymajors = np.linspace(0, 4, 5)
yminors = np.linspace(0, 4, 17)

axes[0].yaxis.set_major_locator(mpl.ticker.FixedLocator(ymajors))
axes[0].yaxis.set_minor_locator(mpl.ticker.FixedLocator(yminors))


# axes[0].xaxis.set_major_locator(mpl.ticker.FixedLocator([]))
# axes[0].xaxis.set_minor_locator(mpl.ticker.FixedLocator(thirds))
  
# axes[0].tick_params(which ='minor', length = 2)
# axes[0].tick_params(which ='minor', length = 4)
# axes[0].tick_params(which ='major', length = 6)
# axes[0].xlabel("Voltage Pulse Rate [kHz]", fontsize = 20)
# axes[0].ylabel('C$_{H}$ [%]', fontsize = 20)

# plt.subplots_adjust(left=0.05, top=1

fig.text(0.08, 0.47, 'C$_{H}$ [at. %]', ha='center', va='center', rotation='vertical',fontsize=20,**arialfont)
fig.text(0.5, -0.03, 'Voltage Pulse Rate [kHz]', ha='center', va='center', rotation='horizontal',fontsize=20,**arialfont)
fig.text(0.078, 0.83, 'a', ha='center', va='center', rotation='horizontal',fontsize=20,**arialfont)
fig.text(0.374, 0.83, 'b', ha='center', va='center', rotation='horizontal',fontsize=20,**arialfont)
fig.text(0.648, 0.83, 'c', ha='center', va='center', rotation='horizontal',fontsize=20,**arialfont)


os.chdir(currentdirectory)
fig.savefig(savefilename, dpi = resolution, bbox_inches='tight')
savefilenamelowres = savefilename + "_lowres"
fig.savefig(savefilenamelowres, dpi = lowresolution, bbox_inches='tight')