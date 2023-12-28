#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 22:54:24 2022

@author: bart924
"""

import matplotlib.pyplot as plt
import os


X1 = (0.5,0.5,0.5)
X2 = (1.0,1.0,1.0)
X3 = (3.0,3.0,3.0)
Y = (50.,125.,200.)
#X, Y = np.meshgrid(X, Y)
Z1 = (4.07,1.29,0.805)
Z2 = (1.89,0.63,0.41)
Z3 = (0.55,0.21,0.13)


plt.scatter(Y,Z1,marker='o',color='k',s=200)
plt.scatter(Y,Z2,marker='s',color='k',s=200)
plt.scatter(Y,Z3,marker='*',color='k',s=200)


plt.xlabel("Voltage Pulse Rate [kHz]", fontsize = 20)
plt.ylabel('C$_{H}$ [%]', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.legend(['DR = 0.5%','DR = 1.0%','DR = 3.0%'], fontsize = 15, frameon = True)

plt.xlim(30,220)
plt.tight_layout()

os.chdir("/Volumes/Dallin_postdoc/GitHub/Dallin_Barton_APT/H_study")
plt.savefig('voltageonlyparameterv2.png', dpi = 1200)