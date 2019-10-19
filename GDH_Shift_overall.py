# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
CA_C=np.abs(CA-CA1)
CA_O=np.abs(CA2-CA1)
ax = plt.subplot(111)
#plt.scatter(HA1[208:400], CA1[208:400], c='g', alpha=0.5)
#plt.scatter(HA[208:400], CA[208:400], c='r', alpha=0.5)
#plt.scatter(HA2[208:400], CA2[208:400], c='b', alpha=0.5)
ax.bar(NUM[145:163],CA_C[145:163],color=["k"])
ax.bar(NUM[164],CA_C[164],width=3,color='g',label='NADH catalytic site')
ax.bar(NUM[165:188],CA_C[165:188],color=["k"])
ax.bar(NUM[189],CA_C[189],width=3,color='b',label='NADH regulatory site')
ax.bar(NUM[203],CA_C[203],color='r')
ax.bar(NUM[204:206],CA_C[204:206],color=["k"])
ax.bar(NUM[207],CA_C[207],width=3,color='r',label='GTP binding site')
ax.bar(NUM[208:247],CA_C[208:247],color=["k"])
ax.bar(NUM[248],CA_C[248],width=3,color='g')
ax.bar(NUM[249:255],CA_C[249:255],color=["k"])
ax.bar(NUM[256],CA_C[256],width=3,color='r')
ax.bar(NUM[257:258],CA_C[257:258],color=["k"])
ax.bar(NUM[259],CA_C[259],width=3,color='r')
ax.bar(NUM[260:285],CA_C[260:285],color=["k"])
ax.bar(NUM[286],CA_C[286],width=3,color='r')
ax.bar(NUM[287:380],CA_C[287:380],color=["k"])
ax.bar(NUM[381],CA_C[381],width=5,color='b')
ax.bar(NUM[282:445],CA_C[282:445],color=["k"])
ax.axhline(y=0.7497,color='k',linestyle='--',dashes=(3,3,2,2))
#plt.arrow(NUM[208], 3.1, 15, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=6 )
ax.arrow(NUM[133], 3.35, 16, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[166], 3.35, 15, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
#plt.arrow(NUM[187], 3.1, 5, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
#plt.arrow(NUM[196], 3.1, 4, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[207], 3.35, 15, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[223], 3.35, 8, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[247], 3.35, 12, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[281], 3.35, 11, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
#plt.arrow(NUM[307], 3.1, 4, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
#plt.arrow(NUM[329], 3.1, 4, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[347], 3.35, 10, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[363], 3.35, 5, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[368], 3.35, 14, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[392], 3.35, 23, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[427], 3.35, 6, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
ax.arrow(NUM[438], 3.35, 27, 0, fc="b", ec="b",width=0.20,head_width=0, head_length=0 )
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
ax.arrow(NUM[157], 3.35, 2, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=1 )
ax.arrow(NUM[240], 3.35, 3, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=2 )
ax.arrow(NUM[263], 3.35, 4, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=2)
ax.arrow(NUM[273], 3.35, 2, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=1 )
ax.arrow(NUM[305], 3.35, 3, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=1 )
ax.arrow(NUM[315], 3.35, 3, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=1 )
ax.arrow(NUM[337], 3.35, 1, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=1 )
ax.arrow(NUM[360], 3.35, 1, 0, fc="k", ec="k",width=0.2,head_width=0.30, head_length=1 )
ax.axhline(y=3.34,linewidth=0.5,color='k')
# Hide the right and top spines
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Only show ticks on the left and bottom spines
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xlabel('Resudue No', fontsize=16)
plt.ylabel('$\Delta$$\delta$ (p.p.m)', fontsize=16)
ax.legend(loc=(0.01,0.67), shadow=False)
#plt.tick_params(top='off', bottom='on', left='on', right='off', labelleft='on', labelbottom='on')
#plt.bar(NUM[208:260],CA_O[208:260])
#plt.savefig('destination_path.png', format='png', dpi=300)
plt.show()
