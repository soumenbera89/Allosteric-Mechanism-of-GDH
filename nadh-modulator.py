#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:40:03 2019

@author: soumen
"""

# -*- coding: utf-8 -*-
"""
Editor : Soumen Bera


"""
from Bio import SeqIO
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, loadtxt
import csv
x = []
y = []
z = []
with open('regulatoryVsnonregulatory.csv', 'r') as f:
    mode = csv.reader(f, delimiter=',')
    for row in mode:
        x.append(int(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
#....................................###.......................
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)
#ax.plot(x,z,color="k", alpha=1, linewidth=1)
#ax.axhline(y=0.0, color='k', linestyle='--', alpha=1, linewidth=0.5)
plot1=ax.plot(x[82:240],y[82:240],linestyle='-',marker='o',markersize=2,color="hotpink", alpha=1, linewidth=0.5, label='With NADH')
plot2=ax.plot(x[82:240],z[82:240],linestyle='-',marker='s',markersize=2,color="dimgray", alpha=1, linewidth=0.5,label='Without NADH')
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
ax.axvspan(x[128], x[158], alpha=0.13, color='gray', lw=0)
ax.axvspan(x[209], x[216], alpha=0.13, color='gray', lw=0)
ax.legend(loc='upper right', fontsize='medium')
fig.tight_layout()
#fig.savefig('NADH-modulator-3A.png', format='png', dpi=600)
plt.show()