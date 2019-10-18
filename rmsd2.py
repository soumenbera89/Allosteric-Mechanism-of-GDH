# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 12:02:38 2019

@author: SOUMEN
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:52:48 2019

@author: SOUMEN
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 06:33:29 2018

@author: SOUMEN
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt, loadtxt
import csv
import math
import pandas as pd
resid=[]
resid1=[]
resid2=[]
resid3=[]
resid4=[]
x= []
x1=[]
y =[]
y1=[]
z= []
z1=[]
x2=[]
y2=[]
z2=[]
x3=[]
y3=[]
z3=[]
x4=[]
y4=[]
z4=[]
with open('open-3jcz.csv', 'r') as f:
    mode = csv.reader(f, delimiter=',')
    for row in mode:
        resid.append(int(row[0]))
        x.append(float(row[1]))
        y.append(float(row[2]))
        z.append(float(row[3]))
##........................................................
with open('jd1.csv', 'r') as g:
    mode1 = csv.reader(g, delimiter=',')
    for row in mode1:
        resid1.append(int(row[0]))
        x1.append(float(row[1]))
        y1.append(float(row[2]))
        z1.append(float(row[3]))
##...........................................................
with open('3jd2.csv', 'r') as h:
    mode2 = csv.reader(h, delimiter=',')
    for row in mode2:
        resid2.append(int(row[0]))
        x2.append(float(row[1]))
        y2.append(float(row[2]))
        z2.append(float(row[3])) 
##.............................................................
with open('3jd3.csv', 'r') as I:
    mode3 = csv.reader(I, delimiter=',')
    for row in mode3:
        resid3.append(int(row[0]))
        x3.append(float(row[1]))
        y3.append(float(row[2]))
        z3.append(float(row[3]))
##...........................................................
with open('3jd4.csv', 'r') as J:
    mode4 = csv.reader(J, delimiter=',')
    for row in mode4:
        resid4.append(int(row[0]))
        x4.append(float(row[1]))
        y4.append(float(row[2]))
        z4.append(float(row[3])) 
n=1
RMSD1=[]
for i in range(496):
    R = np.sqrt(np.sum((x1[i]-x[i])**2+(y1[i]-y[i])**2+(z1[i]-z[i])**2))
    RMSD1.append(R)
RMSD2=[]
for i in range(496):
    R = np.sqrt(np.sum((x2[i]-x[i])**2+(y2[i]-y[i])**2+(z2[i]-z[i])**2))
    RMSD2.append(R)    
RMSD3=[]
for i in range(496):
    R = np.sqrt(np.sum((x3[i]-x[i])**2+(y3[i]-y[i])**2+(z3[i]-z[i])**2))
    RMSD3.append(R)    
RMSD4=[]
for i in range(496):
    R = np.sqrt(np.sum((x4[i]-x[i])**2+(y4[i]-y[i])**2+(z4[i]-z[i])**2))
    RMSD4.append(R)
fig = plt.figure(figsize=(6,3))
ax = fig.add_subplot(1,1,1)
ax.plot(resid4,RMSD3,color='orange',linewidth=0.75,label='Open with GTP & NADH')
ax.plot(resid3,RMSD2,color='cornflowerblue',linewidth=0.75,label='Open without GTP')
ax.axvspan(resid[2],resid[26],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[33],resid[47],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[94],resid[112],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[133],resid[149],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[166],resid[178],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[207],resid[218],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[223],resid[228],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[249],resid[259],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[281],resid[292],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[347],resid[357],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[363],resid[382],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[392],resid[401],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[403],resid[415],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[427],resid[436],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[438],resid[465],alpha=0.3,color='lightgrey',lw=0)
ax.axvspan(resid[470],resid[491],alpha=0.3,color='lightgrey',lw=0)
plt.text(resid[5], 9, r'$\alpha 1$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[33], 9, r'$\alpha 2$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[96], 9, r'$\alpha 3$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[135], 9, r'$\alpha 4$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[165], 9, r'$\alpha 5$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[207], 9, r'$\alpha 6$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[220], 9, r'$\alpha 7$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[246], 9, r'$\alpha 8$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[278], 9, r'$\alpha 9$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[347], 9, r'$\alpha 10$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[365], 9, r'$\alpha 11$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[390], 9, r'$\alpha 12$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[402], 9, r'$\alpha 13$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[427], 9, r'$\alpha 14$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[445], 9, r'$\alpha 15$', fontsize=9, alpha=0.75,rotation=90)
plt.text(resid[475], 9, r'$\alpha 16$', fontsize=9, alpha=0.75,rotation=90)
###.........................................
ax.set_xlabel('Residue Number', fontsize=12)
ax.set_ylabel('Residue RMSD,'r'$\AA$', fontsize=12)
ax.legend(loc='center left', fontsize='xx-small')
fig.tight_layout()    
fig.savefig('Compair_RMSD-2-3.png', format='png', dpi=600)
df = pd.DataFrame({'resid': resid,
                   'RMSD3': RMSD3,
                   'RMSD4':RMSD4})
#df.to_csv('file.csv')