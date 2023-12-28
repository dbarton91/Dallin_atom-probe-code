#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 11:21:49 2022

@author: bart924
"""

#Mass Spectrum Plotting
#This is the file to plot mass spectra from atom probe mass spectrum exported csv's.

#import packages
import pandas as pd # for reading csv's and creating the dataframe
import matplotlib.pyplot as plt #for plotting
import os #for changing the directory

# User inputs
csvfilename = "R31_19708-v04_massspec.csv"
currentdirectory = "Z:/Experimental_results/APT/Fe18Cr14Ni/PWR/R31_19708/recons/SEM_tipprof/default"
savefilename = "82to97" #defaults with .png extension.
resolution = 1200 # resolution for the saved figure in dots per inch. 1200 is usually good.
#List the x range that you would like to plot
xminrange = 81.5
xmaxrange = 97

#Officially, plot only normalized plots. In this code it is against the highest peak (Highest peak is "1" and the rest is a fraction of that)
yminrange = 0.00001 # Low enough to see the background floor but not waste space
ymaxrange = 1.1 #1.1 for the tiny bit of space up top. 

#End of User Inputs

#Start of action
os.chdir(currentdirectory)

df1 = pd.read_csv(csvfilename)

#Normalize the data
uncorrcountall = df1["Uncorrected Count"]
maxcount = uncorrcountall.max()
sumcount = uncorrcountall.sum()
df1["Uncorrected Count"] = df1["Uncorrected Count"]/maxcount

#Plot
plot = df1.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count",color='black',legend=None,fontsize=20)
fig = plot.get_figure()
plt.xlim([xminrange, xmaxrange])
plt.xlabel("m/Q [Da]",fontsize=20)
plt.ylabel("Normalized Counts", fontsize=20)
plt.yscale("log")
plt.ylim([yminrange,ymaxrange])
plt.tight_layout()
plt.show()

#Save
os.chdir(currentdirectory)
fig.savefig(savefilename, dpi = resolution,bbox_inches='tight')


# print(df)