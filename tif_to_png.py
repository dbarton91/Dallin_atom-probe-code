# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 09:30:54 2023

@author: bart924
"""

import os
import multiprocessing as mp
from pathlib import Path
from PIL import Image

def convert_tif_to_png(filepath):
    img = Image.open(filepath)
    newname = Path(filepath).stem
    img.save(f"{newname}.png")

if __name__ == '__main__':
    root = os.getcwd()
    filepaths = []
    for root, dirs, files in os.walk(root):
        for filename in files:
            if filename.endswith(".tif"):
                filepaths.append(os.path.join(root,filename))

    pool = mp.Pool(mp.cpu_count())
    pool.map(convert_tif_to_png, filepaths)
    pool.close()
    pool.join()

print("Done")
