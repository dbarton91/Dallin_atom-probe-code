#Mass Spectrum Plotting
#This is the file to plot mass spectra from atom probe codes

#import packages
import csv #to read csv files
import pandas as pd
import matplotlib.pyplot as plt


csvfilepath = "/Users/bart924/OneDrive - PNNL/Desktop/110121/R31_17898_Mass_Spec_bin1E-2.csv"

df = pd.read_csv(csvfilepath)

uncorrcountall = df["Uncorrected Count"]
maxcount = uncorrcountall.max()
sumcount = uncorrcountall.sum()
df["Uncorrected Count"] = df["Uncorrected Count"]/maxcount*sumcount

# print(df)

hydrogenhunt = df[0:601]

hydrogenhuntuncorrcount = hydrogenhunt["Uncorrected Count"]
maxcountwindow = hydrogenhuntuncorrcount.max()

# print (hydrogenhunt)

df.plot("Mass-to-Charge-State Ratio (Da)","Uncorrected Count",color='black',legend=None)

plt.xlim([0,6])
plt.ylim([0,maxcountwindow])


plt.show()



# print(df)

