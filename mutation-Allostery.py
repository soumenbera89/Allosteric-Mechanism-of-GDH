#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:38:51 2019

@author: soumen
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, loadtxt
import csv
x = []
y = []
z = []
y1= []
z1=[]
with open('mutation-allosteric.csv', 'r') as f:
    mode = csv.reader(f, delimiter=',')
    for row in mode:
        x.append(int(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
        y1.append(float(row[3]))
        z1.append(float(row[4]))
#....................................###.......................
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)
#ax.plot(x,z,color="k", alpha=1, linewidth=1)
#ax.axhline(y=0.0, color='k', linestyle='--', alpha=1, linewidth=0.5)
plot1=ax.plot(x[130:225],z[130:225],linestyle='-',marker='s',markersize=2,color="black", alpha=1, linewidth=0.5,label='Wild Type')
plot2=ax.plot(x[130:225],y[130:225],linestyle='-',marker='s',markersize=2,color="green", alpha=1, linewidth=0.5, label='Gly376Asp')
plot3=ax.plot(x[130:225],y1[130:225],linestyle='-',marker='s',markersize=2,color="darkviolet", alpha=1, linewidth=0.5,label='Arg217Cys')
plot4=ax.plot(x[130:225],z1[130:225],linestyle='-',marker='s',markersize=2,color="brown", alpha=1, linewidth=0.5,label='Ser441Leu')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
#ax.plot(x1[370],y1[370],'bo',markersize=3.5)
#ax.plot(x1[375],y1[375],'bo',markersize=3.5)
#ax.scatter(x2[374],y2[374],color='orange',marker = 'o', s =16)
#ax.scatter(x2[371],y2[371],color='orange',marker = 'o', s =16)
#ax.scatter(x2[204],y2[204],color='orange',marker = 'o', s =16)
#ax.plot(x1[203],y1[203],'bo',markersize=3.5)
ax.set_ylabel('Degree of freedom \n transmission intensity', fontsize=14)
ax.set_xlabel('Residue number', fontsize=14)
ax.axvspan(x[180], x[188], alpha=0.13, color='gray', lw=0)
ax.axvspan(x[159], x[164], alpha=0.13, color='gray', lw=0)
ax.legend(loc='upper right', fontsize='medium')
fig.tight_layout()
#fig.savefig('mutation-3jd4-allostery.png', format='png', dpi=600)
plt.show()