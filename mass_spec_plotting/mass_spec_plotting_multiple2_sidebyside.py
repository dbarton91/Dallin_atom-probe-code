#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 13:02:54 2022

@author: bart924
"""


#Mass Spectrum Plotting
#This is the file to plot mass spectra from atom probe mass spectrum exported csv's.

#import packages
import pandas as pd # for reading csv's and creating the dataframe
import matplotlib.pyplot as plt #for plotting
import os #for changing the directory
import mpl_toolkits.axisartist as axisartist
import numpy as np
import matplotlib.transforms


# User inputs
howmanyplots = 1 #numberofplotsyou want
currentdirectory = "/Volumes/BESECProjectArun/Experimental_results/APT/H_study/Deuterium/Mass_Spectra/Fe18Cr14Ni"
csvfilename1 = "R31_18094-v02_massspec_bin1E-2.csv"
csvfilename2 = "R31_18183-v01_mass_spec.csv"

savefilename = "Fe18Cr14Ni_sidebyside" #defaults with .png extension.

resolution = 1200 # resolution for the saved figure in dots per inch. 1200 is usually good.
lowresolution = 150 # resolution for ppt slides


#List the x range that you would like to plot
xminrange = 0
xmaxrange = 5
#Officially, plot only normalized plots. In this code it is against the highest peak (Highest peak is "1" and the rest is a fraction of that)
yminrange = 0.000001 # Low enough to see the background floor but not waste space
ymaxrange = 1.1 #1.1 for the tiny bit of space up top. 

#End of User Inputs

#Start of action
os.chdir(currentdirectory)

df1 = pd.read_csv(csvfilename1)
df2 = pd.read_csv(csvfilename2)

#Normalize the data
uncorrcountall = df1["Uncorrected Count"]
maxcount = uncorrcountall.max()
sumcount = uncorrcountall.sum()
df1["Uncorrected Count"] = df1["Uncorrected Count"]/maxcount

uncorrcountall2 = df2["Uncorrected Count"]
maxcount2 = uncorrcountall2.max()
sumcount2 = uncorrcountall2.sum()
df2["Uncorrected Count"] = df2["Uncorrected Count"]/maxcount2


#Plot


fig, axes = plt.subplots(nrows=1,ncols=2,sharey=True,figsize=(6.0,3.25))

plot1 = df1.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[0], logy=True, xlim=[0,5], ylim=[0.000001,1], color='black', legend=False, fontsize=15)
plot2 = df2.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[1], logy=True, xlim=[0,5], ylim=[0.000001,1], color='black', legend=False, fontsize=15)

axes[1].set_xlabel("")
axes[0].set_xlabel("")

fig.text(-0.03, 0.5, 'Counts Normalized to $^{56}$Fe$^{2+}$', ha='center', va='center', rotation='vertical',fontsize=15)
fig.text(0.5, -0.01, 'Mass-to-Charge-State Ratio [Da]', ha='center', va='center', rotation='horizontal',fontsize=15)



dx = -43/72.; dy = 0/72. 
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all y ticklabels.
for label in axes[1].yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)

plt.setp(axes[1].get_yticklabels(), ha='left', fontsize=15)

# apply offset transform to all y ticklabels.
for label in axes[0].yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)

plt.setp(axes[0].get_yticklabels(), ha='left', fontsize=15)


# plt.subplots_adjust(left=0.9, top=0)


fig.text(0.164, 0.83, 'g', ha='center', va='center', rotation='horizontal',fontsize=20)
fig.text(0.584, 0.83, 'h', ha='center', va='center', rotation='horizontal',fontsize=20)



# for tick in axes.yaxis.get_majorticklabels():
#     tick.set_horizaontalalignment("left")

# plt.xlim([xminrange, xmaxrange])
# plt.xlabel("Mass-to-Charge-State Ratio [Da]",fontsize=20)
# plt.ylabel("Counts Normalized to $^{58}$Fe$^{2+}$", fontsize=20)
# plt.yscale("log")
# plt.ylim([yminrange,ymaxrange])
# plt.tight_layout()
# plt.show()

#Save
os.chdir(currentdirectory)
fig.savefig(savefilename, dpi = resolution, bbox_inches='tight')
savefilenamelowres = savefilename + "_lowres"
fig.savefig(savefilenamelowres, dpi = lowresolution, bbox_inches='tight')


# print(df)