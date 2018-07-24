import pandas as pd
def load(fn):
    file = open(fn, 'r')
    data = []
    for line in file:
        if line[0] == 'c':
            items = line.rstrip('\n').split('\t')
            data.append(items)
    file.close()
    return data


def writedata(fn, data):
    newdata = data
    df = pd.DataFrame(newdata, columns=['chr', 'indexbp', 'index', 'id', 'bp'])
    df.to_csv(fn, header=None, index=None)
    return


szfn = "sz.txt"
sz = load(szfn)
print "sz loaded"
basefn = "rall.txt"
base = load(basefn)
print "base loaded"
i = 0
for snp in sz:
    snp.append([])
    for line in base:
        if line[1] == snp[3]:
            snp[4] = line[4]
            i = i+1
            break

print "searching finished"

writedata("sz_final.csv",sz)
print len(sz),len(base),i



