#draw fragdist

import os
import sys
import numpy as np
import pandas as pd
import pysam
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn
from optparse import OptionParser
from collections import Counter

#options
parser=OptionParser()
parser.add_option("-i","--input",dest="input",help="your input file name")
parser.add_option("-o","--output",dest="output",help="your output file name")
(options,arg)=parser.parse_args()

#def function

def Fragdistribution(Inbam,outfig):
    sam=os.popen("samtools view -f 0x0002 %s"%Inbam)
    fragL=[]
    for line in sam:
        items=line.rstrip("\n").split('\t')
        flag=items[1]
        flag_length=abs(int(items[8]))
        if (int(flag)==99 or int(flag)==163) and int(flag_length)<=600:
            fragL.append(flag_length)
    count=Counter(fragL)
    fig=plt.figure(figsize=(6.0,4.0))
    df=pd.read_table('./Fragment_length_ratio.txt',header=0,index_col=0).iloc[:,1:]
    for i in range(df.shape[1]-1):
        plt.plot(df.index,df.iloc[:,i+1]/1000,color='#DBDBDB',linestyle='-',linewidth=4)
    plt.plot(count.keys(),np.array(count.values())/float(sum(count.values())),'r')
    plt.xlabel('Insert size (bp)')
    plt.ylabel('Read counts %')

    fig.savefig(outfig)
    plt.close(fig)
    return

#main

Inbam=options.input
outfig=options.output
Fragdistribution(Inbam,outfig)