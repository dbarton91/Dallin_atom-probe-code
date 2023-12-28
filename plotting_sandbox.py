#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:29:40 2022

@author: bart924
"""

import matplotlib.pyplot as plt
import matplotlib.transforms
import numpy as np

fig, ax = plt.subplots(figsize=(12, 6))

x = np.random.random(100)
y = np.random.random(100)

plot1 = plt.plot(x, color='blue')
plt.yscale("log")

plot2 = plt.plot(y, color='black')
plt.yscale("log")


dx = -43/72.; dy = 0/72. 
offset = matplotlib.transforms.ScaledTranslation(dx, dy, fig.dpi_scale_trans)

# apply offset transform to all x ticklabels.
for label in ax.yaxis.get_majorticklabels():
    label.set_transform(label.get_transform() + offset)

plt.setp(ax.get_yticklabels(), ha='left', fontsize=20)

plt.show()




# print(x)