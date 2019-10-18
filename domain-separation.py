# -*- coding: utf-8 -*-
"""
Editor : Soumen Bera


"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, loadtxt
import csv
x = []
y = []
z = []
x1= []
x2= []
y1= []
y2= []
z1= []
z2= []
with open('3jcz-domain-separated.csv', 'r') as f:
    mode = csv.reader(f, delimiter=',')
    for row in mode:
        x.append(int(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))
#resn=np.array(mode[1:])
#resn,mode1,mode2 = loadtxt("3jcz-domain-separated.csv", delimiter=";",usecols=range(3),unpack=True)
with open('3jd3-domain-separated.csv','r') as g:
    mode1 = csv.reader(g, delimiter=',')
    for row in mode1:
        x1.append(int(row[0]))
        y1.append(float(row[1]))
        z1.append(float(row[2]))
with open('3jd4-domain-separated.csv','r') as h:
    model2=csv.reader(h, delimiter=',')
    for row in model2:
        x2.append(int(row[0]))
        y2.append(float(row[1]))
        z2.append(float(row[2]))
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)
#ax.plot(x,z,color="k", alpha=1, linewidth=1)
ax.axhline(y=0.0, color='k', linestyle='--', alpha=1, linewidth=0.5)
plot1=ax.plot(x1,z1,color="b", alpha=1, linewidth=0.5, label='Open metastable state')
plot2=ax.plot(x2,z2,color="orange", alpha=1, linewidth=0.5,label='Closed metastable state')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.plot(x1[370],y1[370],'bo',markersize=3.5)
ax.plot(x1[375],y1[375],'bo',markersize=3.5)
ax.scatter(x2[374],y2[374],color='orange',marker = 'o', s =16)
ax.scatter(x2[371],y2[371],color='orange',marker = 'o', s =16)
ax.scatter(x2[204],y2[204],color='orange',marker = 'o', s =16)
ax.plot(x1[203],y1[203],'bo',markersize=3.5)
ax.set_ylabel('Eigenvectors', fontsize=14)
ax.set_xlabel('Residue', fontsize=14)
ax.axvspan(x1[203], x1[374], alpha=0.13, color='gray', lw=0)
ax.legend(loc='upper right', fontsize='small')
fig.tight_layout()
fig.savefig('normalmode.png', format='png', dpi=600)