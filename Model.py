#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 17:34:17 2018

@author: avinashrperiyavaram
"""

import rasterio
import numpy as np
import csv
filename = 'Draught-Img/yearly/2000mean.tif'
with rasterio.open(filename) as src:
    #read image
    image= src.read()
    # transform image
    bands,rows,cols = np.shape(image)
    image1 = image.reshape (rows*cols,bands)
    print(np.shape(image1))
    # bounding box of image
    l,b,r,t = src.bounds
    #resolution of image
    res = src.res
    res = src.res
    # meshgrid of X and Y
    x = np.arange(l,r, res[0])
    y = np.arange(t,b, -res[0])
    X,Y = np.meshgrid(x,y)
    print (np.shape(X))
    # flatten X and Y
    newX = np.array(X.flatten(1))
    newY = np.array(Y.flatten(1))
    print (np.shape(newX))
    # join XY and Z information
    export = np.column_stack((newX, newY, image1))
    fname='2000mean.csv'
    with open(fname, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerow(["Lattitude" , "Longtitude" , "mean PDSI"])
        a.writerows(export)
        fp.close() # close file

row_count = sum(1 for row in fname)
print (row_count)
