#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 22:54:24 2022

@author: bart924
"""

import matplotlib.pyplot as plt
import os



Y1W26 = (50.,200.) #DR 0.5
Y2W26 = (125) #DR 1
Y3W26 = (50., 200.) #DR 3.0

Y4W25 = (50.,125.) #DR 1.0
Y5W25 = (50.) #DR 2.0




#X, Y = np.meshgrid(X, Y)
Z1W26 = (3.24,1.03) 
Z2W26 = (0.96)
Z3W26 = (0.63,0.38)

Z4W25 = (4.66,2.30) #DR 1
Z5W25 = (2.06) #DR 2




plt.scatter(Y1W26,Z1W26,marker='o',color='k',s=200)
# plt.scatter(Y4W25,Z4W25,marker='o',color='k',s=200)
# plt.scatter(Y2,Z2,marker='s',color='k',s=100)
# plt.scatter(Y5W25,Z5W25,marker='D',color='k',s=200)
plt.scatter(Y3W26,Z3W26,marker='*',color='k',s=200)




plt.xlabel("Voltage Pulse Rate [kHz]", fontsize = 20)
plt.ylabel('C$_{H}$ [%]', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.legend(['DR = 0.5%','DR = 3.0%'], fontsize = 15, frameon = True)

plt.xlim(30,220)
plt.ylim(-0.1,4.2)
plt.tight_layout()

os.chdir("/Volumes/Dallin_postdoc/GitHub/Dallin_Barton_APT/H_study")
plt.savefig('Fe18Cr14Nivoltageonlyparameterv2.png', dpi = 1200)