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
# import mpl_toolkits.axisartist as axisartist
# import numpy as np
import matplotlib.transforms
import numpy as np


# User inputs
howmanyplots = 1 #numberofplotsyou want
currentdirectory = "/Volumes/BESECProjectArun/Experimental_results/APT/H_study/Deuterium/Mass_Spectra/Plotting"
csvfilename1 = "R31_18091-v02_mass_spec.csv"
csvfilename2 = "R31_18094-v02_massspec_bin1E-2.csv"
csvfilename3 = "R31_18698-v01_MassSpec_DR2.0_PR50.csv"
csvfilename4 = "R31_18182-v01_mass_spec.csv"
csvfilename5 = "R31_18183-v01_mass_spec.csv"
csvfilename6 = "R31_18945-v01_mass_spec.csv"

savefilename = "allsix" #defaults with .png extension.

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
df3 = pd.read_csv(csvfilename3)
df4 = pd.read_csv(csvfilename4)
df5 = pd.read_csv(csvfilename5)
df6 = pd.read_csv(csvfilename6)


#Normalize the data
def normalizethedata(dummydf):
    
    uncorrcountall = dummydf["Uncorrected Count"]
    maxcount = uncorrcountall.max()
    dummydf["Uncorrected Count"] = dummydf["Uncorrected Count"]/maxcount
    
    return(dummydf)
    
df1 = normalizethedata(df1)
df2 = normalizethedata(df2)
df3 = normalizethedata(df3)
df4 = normalizethedata(df4)
df5 = normalizethedata(df5)
df6 = normalizethedata(df6)


#Plot
fig, axes = plt.subplots(nrows=2,ncols=3,figsize=(9.75,3.25), sharex='col', sharey='row')

# unpack all the axes subplots
axes = axes.ravel()

plot1 = df1.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[0], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot2 = df2.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[1], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot3 = df3.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[2], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot4 = df4.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[3], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot5 = df5.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[4], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot6 = df6.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[5], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")


fig.text(-0.02, 0.9, 'Counts Normalized to $^{56}$Fe$^{2+}$', ha='center', va='center', rotation='vertical',fontsize=20)
fig.text(0.5, -0.03, 'Mass-to-Charge-State Ratio [Da]', ha='center', va='center', rotation='horizontal',fontsize=20)

axes[3].xaxis.set_ticks(np.arange(0, 6, 1))
axes[4].xaxis.set_ticks(np.arange(0, 6, 1))
axes[5].xaxis.set_ticks(np.arange(0, 6, 1))

axes[0].yaxis.set_ticks([0.000001,0.00001,0.0001,0.001,0.01,0.1,1])
axes[3].yaxis.set_ticks([0.000001,0.00001,0.0001,0.001,0.01,0.1,1])

locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=12)
axes[0].yaxis.set_minor_locator(locmin)
axes[0].yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

axes[3].yaxis.set_minor_locator(locmin)
axes[3].yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

dx = -33/72.; dy = 2/72. 
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all y ticklabels.
for label in axes[3].yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)

plt.setp(axes[3].get_yticklabels(), ha='left', fontsize=15)

# apply offset transform to all y ticklabels.
for label in axes[0].yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)

plt.setp(axes[0].get_yticklabels(), ha='left', fontsize=15)


plt.subplots_adjust(left=0.05, top=1.65)


fig.text(0.072, 1.58, 'a', ha='center', va='center', rotation='horizontal',fontsize=20)
fig.text(0.372, 1.58, 'b', ha='center', va='center', rotation='horizontal',fontsize=20)
fig.text(0.672, 1.58, 'c', ha='center', va='center', rotation='horizontal',fontsize=20)
fig.text(0.072, 0.75, 'd', ha='center', va='center', rotation='horizontal',fontsize=20)
fig.text(0.372, 0.75, 'e', ha='center', va='center', rotation='horizontal',fontsize=20)
fig.text(0.672, 0.75, 'f', ha='center', va='center', rotation='horizontal',fontsize=20)


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