# -*- coding: utf-8 -*-
"""
Created on Sat May 26 15:11:51 2018

@author: SOUMEN
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
NUM=[]
CA=[]
HA=[]
RES=[]
CB=[]
CO=[]
N=[]
H=[]
HA=[]
NUM, RES, CA, CB, CO, N, H, HA  = genfromtxt('3jd4_shiftx.csv', delimiter=',',skip_header=2, unpack=True)
NUM1, RES1, CA1, CB1, CO1, N1, H1, HA1  = genfromtxt('3jcz_shiftx.csv', delimiter=',',skip_header=1, unpack=True)
NUM2, RES2, CA2, CB2, CO2, N2, H2, HA2  = genfromtxt('3jd3_shiftx.csv', delimiter=',',skip_header=1, unpack=True)
ax = plt.subplot(111)
plt.scatter(H2[451:453],N2[451:453],s=150,facecolors='none',edgecolors="blue",alpha=0.5)
plt.scatter(H[451:453],N[451:453],s=150,facecolors='none',edgecolors="orange",alpha=0.5)
plt.scatter(H2[366:368],N2[366:368],s=150,facecolors='none',edgecolors="blue",alpha=0.5)
plt.scatter(H[366:368],N[366:368],s=150,facecolors='none',edgecolors="orange",alpha=0.5)
plt.show()