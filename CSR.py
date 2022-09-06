
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import stuff
from math import sqrt, log, exp
import random
import numpy as np
import decimal
import pandas as pd

D = decimal.Decimal 

#initialize stuff
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
filename = filename

#Load the CSV file into Python.
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

columnx = df.iloc[:,0]
columny = df.iloc[:,1]
columnz = df.iloc[:,2]
columnmass = df.iloc[:,3]


print('Finished column loading')

lencolumn = len(columnmass)
n = 0
newcolumnmass = []

randomlist = random.sample(range(lencolumn),lencolumn)

while n < lencolumn:
    
    
    randomnumber = randomlist[n]
    nextentry = df.iloc[randomnumber,3]
    newcolumnmass.append(nextentry)
    
    n += 1
    ntest = n % 100000
    
    if ntest == 0:
        print('Random Number Loading: ' + repr(n))

df.iloc[:,3] = newcolumnmass

print('Finished mass assignment randomizing')


volumeold = 0
n = 0

howmanyatoms = len(columnx)


K = 2
r = 0
dr = 0.001
roh = 74
Pi=3.141592653589793238462643383
xstor = []
ystor = []
zstor = []
mass = []
k = 1

# Step one, step up atom and step up radius

K += 1
r += dr

#Step two, calculate probability


for n in range(howmanyatoms):
#   Define probability
 
    randomnumber = 1
    P = 0
    volumeold = 0
   
    while randomnumber > P:
        
        randomnumber = random.random()
        storageK = []
        storageP = []
                
        #Expanded version of the probability and a log taken and Stirlings approximation applied

        firststep = D(log(3))
        secondstep = D((K-1)*(log(K-1)))-D(K-1)
        fourthstep = D(K*log(4*Pi/3*roh))
        fifthstep = D((3*K-1)*log(r))
        sixthstep = D(4*Pi/3*roh*pow(r,3))
        
        logofP = firststep-secondstep+fourthstep+fifthstep-sixthstep
        
# Python cannot take exponents of negatives
        try:
            P = exp(logofP)
        except:
            try:
                logofP = -logofP
                P = 1/exp(logofP)
# If all else fails, punt
            except: P = 0.001
                  
        if randomnumber > P:

#This means the probability is not high enough, so we need to increase the radius to   #increase the probability.  

            r +=dr
                        
            
        else:
            
#This means the probability is high enough, so we add another atom at the same radius #and see if we can do it again.
            
# We randomly pick a number for x and then use 3-D Pythagorean theorem to #find y #and z. The problem with this method is that as x is randomly chosen it limits the #possible options for y and z to be an extreme e.g. 1/n chance for x to be 0.0. 1/n^2 #chance for x and y to be 0.0 allowing z to be 1. To overcome this, I just brute forced all #of the possible combinations of randomly choosing a point in space. The dataset is #large enough to get over the statistical variance this causes. 

            if k == 1:
            
                x = r * random.random()
                if random.random() < 0.50:
                    x=-x
                y = sqrt(pow(r,2) - pow(x,2)) * random.random()
                if random.random() < 0.50:
                    y=-y
                z = sqrt(pow(r,2) - pow(x,2) - pow(y,2))
                if random.random() < 0.50:
                    z=-z
                
            if k == 2:
                
                x = r * random.random()
                if random.random() < 0.50:
                    x=-x
                z = sqrt(pow(r,2) - pow(x,2)) * random.random()
                if random.random() < 0.50:
                    z=-z
                y = sqrt(pow(r,2) - pow(x,2) - pow(z,2))
                if random.random() < 0.50:
                    y=-y
                
            if k == 3:
                
                    
                y = r * random.random()
                if random.random() < 0.50:
                    y=-y
                x = sqrt(pow(r,2) - pow(y,2)) * random.random()
                if random.random() < 0.50:
                    x=-x
                z = sqrt(pow(r,2) - pow(x,2) - pow(y,2))
                if random.random() < 0.50:
                    z=-z
                    
            if k == 4:
                    
                y = r * random.random()
                if random.random() < 0.50:
                    y=-y
                z = sqrt(pow(r,2) - pow(y,2)) * random.random()
                if random.random() < 0.50:
                    z=-z
                x = sqrt(pow(r,2) - pow(y,2) - pow(z,2))
                if random.random() < 0.50:
                    x=-x
                      
            if k == 5:
                    
                z = r * random.random()
                if random.random() < 0.50:
                    z=-z
                x = sqrt(pow(r,2) - pow(z,2)) * random.random()
                if random.random() < 0.50:
                    x=-x
                y = sqrt(pow(r,2) - pow(x,2) - pow(z,2))
                if random.random() < 0.50:
                    y=-y  
                    
                    
            if k == 6:    
          
                z = r * random.random()
                if random.random() < 0.50:
                    z=-z
                y = sqrt(pow(r,2) - pow(z,2)) * random.random()
                if random.random() < 0.50:
                    y=-y
                x = sqrt(pow(r,2) - pow(z,2) - pow(y,2))
                if random.random() < 0.50:
                    x=-x
                
            
            k += 1
            
            if k > 6:
                k = 1
            
            K += 1
            
            xstor.append(x)
            ystor.append(y)
            zstor.append(z)
            
            
            randommass = random.random()*300
            mass.append(randommass)
            
            Ktest = K% 100000
            if Ktest == 0:
                print ('K: ' + repr(K))
       
#This is for IVAS to work with. The extremes are now at the origin.    
xstor = np.array(xstor)
xstor = xstor - min(xstor) 
ystor = np.array(ystor)
ystor = ystor - min(ystor)
zstor = np.array(zstor)
zstor = zstor - min(zstor)
        
#Change the positions. The mass has already been taken care of.
df.iloc[:,0] = xstor 
df.iloc[:,1] = ystor 
df.iloc[:,2] = zstor 


print ("Column Loading Finished")

#Save to a new CSV
df.to_csv('newfilename', sep=',',index=False)
#end of code
