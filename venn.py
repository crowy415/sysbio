def norm(a):
    ans=[0,0]
    if a[0] > a[1]:
        t = a[0]
        ans[0] = a[0] / t
        ans[1] = a[1] / t
    else:
        t = a[1]
        ans[0] = a[0] / t
        ans[1] = a[1] / t
    return ans

def update(b):
    ans=[0,0]
    tmp1 = b[0]
    tmp2 = b[1]
    ans[0] = -0.5*tmp2
    ans[1] = 1.0/3.0*tmp1+5.0/6.0*tmp2
    return ans

y=[]
y.append([1.0,1.0])
x=[]
x.append([])
x.append(update(y[0]))
y.append(norm(x[1]))
x.append(update(y[1]))

eps=0.0001
i=2
while True:
    if (abs(x[i][1]-x[i-1][1])>=eps):
        y.append(norm(x[i]))
        x.append(update(y[i]))
        print i,y[i],x[i+1]
        i=i+1
    else:
        break




