#description: plot insert size
#name: crowy

import os
import pandas as pd
import numpy as np
import pysam
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from optparse import OptionParser

#read file
insert_size=[]
fn="Nd27.pe.q10.sort.rmdup.bam"
input=pysam.AlignmentFile(fn)
for read in input.fetch(until_eof=True):
    if abs(read.template_length) < 600:
        insert_size.append(abs(read.template_length))
data=np.array(insert_size)
np.save(fn+".npy",data)
sns.set_style('white')
ax=sns.distplot(data,hist=False,norm_hist=True)
ax.set_xlabel('Insert size (bp)')
ax.set_ylabel('Density')
fig=ax.get_figure()
fig.savefig(fn+".png")



