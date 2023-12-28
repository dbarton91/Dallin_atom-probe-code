#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 22:54:24 2022

@author: bart924
"""

import matplotlib.pyplot as plt
import os
import matplotlib.axes as ax


X1 = (0.5,0.5,0.5)
X2 = (3.0,3.0,3.0)
Y = (50.,200.)
#X, Y = np.meshgrid(X, Y)
Z1 = (5.77,1.86)
Z2 = (0.79,0.26)

# yticklabels = (0.0,1.0,2.0,3.0,4.0,5.0,6.0)

plt.scatter(Y,Z1,marker='o',color='k',s=200)
plt.scatter(Y,Z2,marker='*',color='k',s=200)
#plt.scatter(Y,Z3,marker='+',color='k',s=100)

# ax.set_yticks(0.0,6.0)


plt.xlabel("Laser Pulse Rate [kHz]", fontsize = 20)
plt.ylabel('C$_{H}$ [%]', fontsize = 20)
plt.xticks(fontsize = 20)
plt.yticks(fontsize = 20)

plt.legend(['DR = 0.5%','DR = 3.0%'], fontsize = 15, frameon = True)

plt.xlim(30,220)
plt.ylim(-0.1,6.5)
plt.tight_layout()


# plt.ticklabel_format(axis='y',style='sci',)


os.chdir("/Volumes/Dallin_postdoc/GitHub/Dallin_Barton_APT/H_study")
plt.savefig('laseronlyparameterv2.png', dpi = 1200)