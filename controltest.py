import pandas as pd
import random
file = open('control.vcf','r')
length = 0
data = []
amount = 3482
for line in file:
    if line[0] != '#':
        length = length+1
        item = line.rstrip('\n').split('\t')
        data.append(['chr'+item[0],item[1]])

num = random.sample(range(1,length),amount)
newdata = []
for i in range(0,amount):
    newdata.append(data[num[i]-1])

df = pd.DataFrame(newdata,columns = ['chr','position'])
df.to_csv('random.csv',header=None,index=None)
print("finished")




