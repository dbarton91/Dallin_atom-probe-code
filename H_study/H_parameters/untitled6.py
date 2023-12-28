

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
Y2 = (50.,200.)
#X, Y = np.meshgrid(X, Y)
Z1 = (4.07,1.29,0.805)
Z2 = (1.89,0.63,0.41)
Z3 = (0.55,0.21,0.13)

Z4 = (5.77,1.86)
Z5 = (0.79,0.26)

plt.plot(Y,Z1,marker='o',color='k',markersize=8,linestyle=':')
plt.plot(Y,Z2,marker='s',color='k',markersize=8,linestyle=':')
plt.plot(Y,Z3,marker='*',color='k',markersize=8,linestyle=':')
plt.plot(Y2,Z4,marker='o',color='r',markersize=8,linestyle='none')
plt.plot(Y2,Z5,marker='*',color='r',markersize=8,linestyle='none')

plt.xlabel("Pulse Rate [kHz]", fontsize = 20)
plt.ylabel('C$_{H}$ [%]', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.legend(['Volt DR = 0.5%','Volt DR = 1.0%','Volt DR = 3.0%','Laser DR = 0.5%', 'Laser DR = 3%'], fontsize = 15, frameon = True)

plt.xlim(30,220)
plt.ylim(-0.1,6.5)
plt.tight_layout()

os.chdir("/Volumes/Dallin_postdoc/GitHub/Dallin_Barton_APT/H_study")
plt.savefig('bothparameters.png', dpi = 1200)