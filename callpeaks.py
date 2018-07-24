import os
from optparse import OptionParser
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import random
from collections import Counter


#adaptable parameters
gsize="hs"
pval=2
fval=1
qval=5
ubool=False
width=500
pipeup=10
bl="./Data/Ref/hg19_blacklist.bed"


#options
parser=OptionParser()
parser.add_option("-i","--input",dest="input",help="you input file name")
parser.add_option("-o","--outdir",dest="output",help="you output file direction")
(options,arg)=parser.parse_args()
fn=options.input


#def functions
def Mkdir(path):
    path=path.strip()
    path=path.rstrip('\\')
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False
        
        
def Macs2(inbed,gsize,outdir,name):
    os.system("macs2 callpeak -t %s -f BED -g %s --outdir %s -q 0.01 -n %s --nomodel --shift 0"
             %(inbed,gsize,outdir,name))
    return
    
    
def HQpeaks(inxls,insummits,inbed,pval,fval,qval,ubool,width,pipeup):
    xls=open(inxls,'r')
    summits=open(inbed,'r')

    outxls=open(inxls[:-4]+".HQ.xls",'w')
    outxls.write("chr\tstart\tend\tlength\tabs_summit\tpileup\t-10*log10(pvalue)\tfold_enrichment\t-10*log10(qvalue)\tname\n")
    outbed=open(inbed[:-11]+".HQ.bed",'w')
    outsummits=open(insummits[:-4]+".HQ.bed",'w')
    for line in xls:
        if re.search(r"^#",line) or re.search(r"^\n",line) or re.search(r"start|end",line):
            continue
        else:
            linesummits=summits.readline()
            items=line.rstrip('\n').split('\t')
            if (float(items[5])>float(pipeup) and float(items[6])>float(pval) and float(items[7])>float(fval) and float(items[8])>float(qval)):
                summit=int(items[4])
                if ubool:
                    start=int(items[1])
                    end=int(items[2])
                else:
                    width=int(width)
                    start=summit-width/2
                    end=summit+width/2
                linebed=items[0]+'\t'+str(start)+'\t'+str(end)+'\t'+items[9]+'\t'+items[8]+'\n'
                outbed.write(linebed)
                outxls.write(line)
                outsummits.write(linesummits)
    xls.close()
    summits.close()
    outxls.close()
    outbed.close()
    outsummits.close()
    
    
def rmBL(inbed,blbed,finalbed):
    os.system("bedtools intersect -a %s -b %s -v > %s"%(inbed,blbed,finalbed))
    return    
    
    
#main
input=options.input
output=options.output
xls_dir=ogname+"_peaks.xls"
summits_dir=ogname+'_summits.bed'
bed_dir=ogname+"_peaks.narrowPeak"
HQpeaks(xls_dir,summits_dir,bed_dir,options.p1,options.f1,options.q1,options.u,options.w,options.pipeup)
hqbed=ogname+"_peaks.HQ.bed"
hqrmblbed=ogname+'_peaks.final.bed'
bl=ref_index+'.blacklist.bed'
rmBL(hqbed,bl,hqrmblbed)





    

