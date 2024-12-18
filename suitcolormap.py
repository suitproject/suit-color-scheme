#!/usr/bin/env python3

from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from astropy.io import fits
import glob
import numpy as np

def make_cmap(col_ls, pos_ls=None):
    if (pos_ls != None):
       cmap= LinearSegmentedColormap.from_list("CustomGradient1", list(zip(pos_ls, col_ls)))
    else:
        cmap= LinearSegmentedColormap.from_list("CustomGradient1", col_ls)
    return(cmap)

filterColor = {
    'BB01': make_cmap(['#000000','#35095f','#e8acf3','#ffffff'], [0, 0.26, 0.7, 1]),
    'BB02': make_cmap(['#000000','#562210','#be8b12','#ffffff']),
    'BB03': make_cmap(['#000000','#6d0000','#d39552','#ffffff']),
    'NB01': make_cmap(['#000000','#ffffff']),
    'NB02': make_cmap(['#000000','#3e600c','#a4d15e','#ffffff']),
    'NB03': make_cmap(['#000000','#672000','#ffc600','#ffffff'], [0,0.34,0.68,1]),
    'NB04': make_cmap(['#000000','#674201','#dfbe0b','#ffffff']),
    'NB05': make_cmap(['#000000','#763200','#ff9600','#ffffff'], [0,0.24,0.57,1]),
    'NB06': make_cmap(['#000000','#005393','#68b0d6','#ffffff'], [0,0.38,0.66,1]),
    'NB07': make_cmap(['#000000', '#aa4639', '#ffffff']),
    'NB08': make_cmap(['#000000','#075c66','#7adeff','#ffffff'], [0,0.38,0.66,1])
}
