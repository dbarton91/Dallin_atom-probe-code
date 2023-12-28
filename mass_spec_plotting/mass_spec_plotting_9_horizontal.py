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
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

# User inputs
howmanyplots = 1 #numberofplotsyou want
currentdirectory = "/Volumes/BESECProjectArun/Experimental_results/APT/H_study/H_DR_PR_parameterstudy/Mass_Spectra/Pure_Fe"
csvfilename1 = "R31_18807-v01_mass_spec_DR0.5_PR50.csv"
csvfilename2 = "R31_18807-v01_mass_spec_DR0.5_PR125.csv"
csvfilename3 = "R31_18807-v01_mass_spec_DR0.5_PR200.csv"
csvfilename4 = "R31_18807-v01_mass_spec_DR1.0_PR50.csv"
csvfilename5 = "R31_18807-v01_mass_spec_DR1.0_PR125.csv"
csvfilename6 = "R31_18807-v01_mass_spec_DR1.0_PR200.csv"
csvfilename7 = "R31_18807-v01_mass_spec_DR3.0_PR50.csv"
csvfilename8 = "R31_18807-v01_mass_spec_DR3.0_PR125.csv"
csvfilename9 = "R31_18807-v01_mass_spec_DR3.0_PR200.csv"




savefilename = "PureFeAll9_horizontal" #defaults with .png extension.

resolution = 1200 # resolution for the saved figure in dots per inch. 1200 is usually good.
lowresolution = 150 # resolution for ppt slides


#List the x range that you would like to plot
xminrange = 0
xmaxrange = 5
#Officially, plot only normalized plots. In this code it is against the highest peak (Highest peak is "1" and the rest is a fraction of that)
yminrange = 0.000005 # Low enough to see the background floor but not waste space
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
df7 = pd.read_csv(csvfilename7)
df8 = pd.read_csv(csvfilename8)
df9 = pd.read_csv(csvfilename9)


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
df7 = normalizethedata(df7)
df8 = normalizethedata(df8)
df9 = normalizethedata(df9)


#Plot
fig, axes = plt.subplots(nrows=1,ncols=9,figsize=(10 ,2), sharex='col', sharey='row')

# unpack all the axes subplots
axes = axes.ravel()

plot1 = df1.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[0], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot2 = df2.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[1], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot3 = df3.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[2], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot4 = df4.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[3], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot5 = df5.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[4], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot6 = df6.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[5], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot7 = df6.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[6], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot8 = df6.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[7], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")
plot9 = df6.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count", ax=axes[8], logy=True, xlim=[xminrange,xmaxrange], ylim=[yminrange,ymaxrange], color='black', legend=False, fontsize=15, xlabel="")

fig.text(-0.02, 0.9, 'Counts', ha='center', va='center', rotation='vertical',fontsize=20)
fig.text(0.48, -0.03, 'm/Q', ha='center', va='center', rotation='horizontal',fontsize=16)


minorLocator = MultipleLocator(1)
for n in range(9):
    axes[n].xaxis.set_minor_locator(minorLocator)

# axes[3].xaxis.set_ticks(np.arange(0, 6, 1))
# axes[4].xaxis.set_ticks(np.arange(0, 6, 1))
# axes[5].xaxis.set_ticks(np.arange(0, 6, 1))
# for n in range(9):
#     axes[n].xaxis.set_ticks(np.arange(0, 6, step=1))
    
# for n in range(9):
#     axes[n].xaxis.set_ticklabels([,1,2,3,4,5])

# locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=12)

# for n in range(9):
#     axes[n].yaxis.set_minor_locator(locmin)
#     axes[n].yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())

# dx = -33/72.; dy = 2/72. 
# offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# # apply offset transform to all y ticklabels.
# for label in axes[3].yaxis.get_majorticklabels():
#     label.set_transform(label.get_transform() + offset)

# plt.setp(axes[3].get_yticklabels(), ha='left', fontsize=15)

# # apply offset transform to all y ticklabels.
# for label in axes[0].yaxis.get_majorticklabels():
#     label.set_transform(label.get_transform() + offset)

# plt.setp(axes[0].get_yticklabels(), ha='left', fontsize=15)


plt.subplots_adjust(left=0.05, top=1.65)

falldown = 0
fallover = 0.0961
startvert = 1.58
starthoriz = 0.06
fig.text(starthoriz, startvert, 'i', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover, startvert-falldown, 'ii', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*2, startvert-falldown*2, 'iii', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*3, startvert-falldown*3, 'iv', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*4, startvert-falldown*4, 'v', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*5, startvert-falldown*5, 'vi', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*6, startvert-falldown*6, 'vii', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*7, startvert-falldown*7, 'viii', ha='left', va='center', rotation='horizontal',fontsize=20)
fig.text(starthoriz+fallover*8, startvert-falldown*8, 'ix', ha='left', va='center', rotation='horizontal',fontsize=20)

# fig.text(-0.02, startvert, 'a', ha='center', va='center', rotation='horizontal',fontsize=30)


# starthoriz = 0.58
# fontsizeselection = 13
# fig.text(starthoriz, startvert, 'DR = 0.5%, PR = 50 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown, 'DR = 0.5%, PR = 125 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*2, 'DR = 0.5%, PR = 200 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*3, 'DR = 1.0%, PR = 50 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*4, 'DR = 1.0%, PR = 125 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*5, 'DR = 1.0%, PR = 200 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*6, 'DR = 3.0%, PR = 50 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*7, 'DR = 3.0%, PR = 125 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)
# fig.text(starthoriz, startvert-falldown*8, 'DR = 3.0%, PR = 200 kHz', ha='center', va='center', rotation='horizontal',fontsize=fontsizeselection)



# for tick in axes.yaxis.get_majorticklabels(): 
#     tick.set_horizaontalalignment("left")

# plt.xlim([xminrange, xmaxrange])
# plt.xlabel("Mass-to-Charge-State Ratio [Da]",fontsize=20)
# plt.ylabel("Counts Normalized to $^{58}$Fe$^{2+}$", fontsize=20)
# plt.yscale("log")
# plt.ylim([yminrange,ymaxrange])
# plt.tight_layout()
# plt.show()

# Save
os.chdir(currentdirectory)
fig.savefig(savefilename, dpi = resolution, bbox_inches='tight')
savefilenamelowres = savefilename + "_lowres"
fig.savefig(savefilenamelowres, dpi = lowresolution, bbox_inches='tight')


# print(df)