x=[]
y=[1.0]
for i in range(0,5):
    x.append(2.0+0.2*i)
    k1=x[i]/y[i]
    k2=(x[i]+0.5*0.2)/(y[i]+0.5*0.2*k1)
    k3=(x[i]+0.5*0.2)/(y[i]+0.5*0.2*k2)
    k4=(x[i]+0.5*0.2)/(y[i]+0.5*0.2*k3)
    temp=y[i]+0.2/6*(k1+2*k2+2*k3+k4)
    y.append(temp)
print x,y

