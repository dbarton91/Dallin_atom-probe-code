#Mass Spectrum Plotting
#This is the file to plot detector hit histogram data from atom probe codes

#import packages
import csv #to read csv files
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import kde
import numpy as np
import seaborn as sns
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d import axes3d


# Read in the csv

# Label the csv
csvfilepath = '/Users/bart924/OneDrive - PNNL/Desktop/R31_17597_DetectorEvents.csv'
# Read in the csv
df = pd.read_csv(csvfilepath)

# Separate the csv
x = df["Detector X (mm)"]
y = df["Detector Y (mm)"]
z = df["Count"]
maxz = max(z)
df["Count"] = df["Count"]/maxz
# print(z[377])

maxx = max(x)
minx = min(x)
maxy = max(y)
miny = min(y)
xaxisticks = np.linspace(maxx,minx, num = 5)

print(maxx)

pivot = df.pivot(index='Detector X (mm)', columns='Detector Y (mm)', values='Count')

# ax = sns.heatmap(pivot)

# plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x,y,z, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(x,y,z, c='red')
plt.show()

# X,Y = np.meshgrid(x,y)
# Z = np.meshgrid(z)

# print(X,Y)
# # print(z)
# # plt.scatter(x,y,z)

# # plt.contour(X,Y,Z)

# plt.show()



