import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn



def CorrFig(data,outname):
    data.corr().to_csv(outname+'.corr',index=True,header=True,sep='\t')
    seaborn.set_context('notebook', font_scale=1.2)
    fig1 = seaborn.clustermap(data.corr(), method='average', metric='euclidean', figsize=(12,12), cmap='YlGnBu', annot=True)
    plt.setp(fig1.ax_heatmap.yaxis.get_majorticklabels(), rotation=0)
    plt.setp(fig1.ax_heatmap.xaxis.get_majorticklabels(), rotation=90)
    plt.savefig(outname+'.corr.pdf')
    return

count_norm = 'atac.count.log.norm'
count_norm_df=pd.read_table(count_norm,header=0,index_col=0)
CorrFig(count_norm_df,count_norm)