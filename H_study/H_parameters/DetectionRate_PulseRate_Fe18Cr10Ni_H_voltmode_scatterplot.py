#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 19:03:10 2022

@author: bart924
"""

import matplotlib.pyplot as plt
import os

Y1W16 = (50.,200.) #DR 0.5
Y2W16 = (50.,125.,200.) #DR 3


#X, Y = np.meshgrid(X, Y)
Z1W16 = (3.61,0.98)  #DR 0.5
Z2W16 = (0.39,0.30,0.41) #DR 3

plt.scatter(Y1W16,Z1W16,marker='o',color='k',s=200)
plt.scatter(Y2W16,Z2W16,marker='*',color='k',s=200)

plt.xlabel("Voltage Pulse Rate [kHz]", fontsize = 20)
plt.ylabel('C$_{H}$ [%]', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.legend(['DR = 0.5%','DR = 3.0%'], fontsize = 15, frameon = True)

plt.xlim(30,220)
plt.ylim(-0.1,4.2)
plt.tight_layout()

os.chdir("/Volumes/Dallin_postdoc/GitHub/Dallin_Barton_APT/H_study")
plt.savefig('Fe18Cr10Nivoltageonlyparameterv2.png', dpi = 1200)