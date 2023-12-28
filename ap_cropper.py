#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 10:00:45 2022

@author: bart924
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import os

os.getcwd()


def ap_cropper(pathfile): #string. confirm the directory
    name = pathfile
    file_name_without_extension = os.path.splitext(name)[0]
    savename = file_name_without_extension + "_cropped.png"
    img = np.array(Image.open(name))
    #Get the length of pixels of the rectange
    shape = img.shape[1]
    shapehalf = int(shape/2)
    #Is is for the x it's actually the y-axis
    shapex = img.shape[0]
    shapexhalf = int(shapex/2)
    #Start big. If there is a mistake, it will throw a bomb error
    top = 10000000
    bottom = 10000000
    left = 10000000
    right = 10000000
    #The for loops is to scan from top to bottom. Mostly unnecessary looking for
    #The extra pixel if it is slanted. It should cut at the most extreme edge
    #Count from the top
    for a in range(shape):
        n=0
        while img[n,a][1] == 255 and n < shapex-10:
            n = n+1   
        if n < top:
            top = n
    top = top - 5
    #Count from the bottom   
    for a in range(shape):
        m=0
        while img[-m,a][1] == 255 and m < shapex-10:
            m = m+1
        if m < bottom:
           bottom = m 
    bottom = shapex-bottom
    bottom = bottom +5
    #Count from the left
    for a in range(shapex):
        o=0
        while img[a,o][0] == 255 and o < shape-10:
            o = o+1
        if o < left:
            left = o
    left = left - 5
    #Count from the right
    for a in range(shapex):
        p=0
        while img[a,-p][0] == 255 and p < shape-10:
            p = p+1
        if p < right:
            right = p 
    right = shape - right
    right = right + 5
    #crop and save
    img0 = Image.fromarray(img)
    img0 = img0.crop((left, top, right, bottom))
    img0.save(savename)
    
    return

image_directory = "X:\\Experimental_results\\APT\\NETL\\DT2\\liftout2\\R5115_00474\\tobecropped"

for filename in os.listdir(image_directory):
    if filename.endswith(".PNG") or filename.endswith(".png"):
        file_path = os.path.join(image_directory, filename)
        ap_cropper(file_path)

# ap_cropper("Fe_box.PNG")
# ap_cropper("H_box.PNG")
# ap_cropper("H2_box.PNG")


