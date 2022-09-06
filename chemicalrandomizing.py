#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import stuff
import pandas as pd
from sqlalchemy import create_engine
import random
import sqlite3
from pandas.io import sql
import subprocess
import numpy as np
import uuid
import csv
import os

#set constants    
total_sum = 0
loading = 0
loadingcvs = 0
maxx = 0
maxy = 0
maxz = 0
minx = 0
miny = 0
minz = 0
chunksize = 10000
i = 0
j = 1

#define your file name
#filename = filename

#Read in your CSV file

loading = 0
chunks = []
for chunk in pd.read_csv(filename, chunksize=chunksize, low_memory=False):
    chunks.append(chunk)
    loading +=1
    loadingtest = loading % 100
    if loadingtest == 0:
        print ("Loading: " + repr(loading))
df = pd.concat(chunks, axis=0)

print('Finished Loading')

#After you are finished loading, create a dataframe putting x, y, z and mass into columns 0, 1, 2, #and 3.

columnx = df.iloc[:,0]
columny = df.iloc[:,1]
columnz = df.iloc[:,2]
columnmass = df.iloc[:,3]

print('Finished column loading')

lencolumn = len(columnmass)
n = 0
newcolumnmass = []

#The random sample will pick numbers randomly from a list given and not repeat that list. Here, #the list length was taken, a number from that list length randomly chosen, the position from the #mass-to-charge ratio column was taken, then that position was added to a new column.

randomlist = random.sample(range(lencolumn),lencolumn)

while n < lencolumn:
    
    randomnumber = randomlist[n]
    nextentry = df.iloc[randomnumber,3]
    newcolumnmass.append(nextentry)
    n += 1
    ntest = n % 100000
    
    if ntest == 0:
        print('Random Number Loading: ' + repr(n))

#Reload the chosen mass into a new column
df.iloc[:,3] = newcolumnmass
print('Finished column randomizing')

#Write back to a CSV file.
df.to_csv('APT_shuffled.csv', sep=',',index=False)
#end of code
