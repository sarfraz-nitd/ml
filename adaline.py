w=[0.1,0.2,0.15,0.3]
a=0.2
st=[[[0.2,0.1,0.3,0.4],1.0],
    [[0.3,0.1,0.2,0.2],2.0],
    [[0.2,0.1,0.4,0.3],1.5],
    [[0.3,0.2,0.4,0.2],2.1]]
b=0.5
for i in range(8):
    print "Iteration :",i
    for sti in st:
        t=sti[1]
        x=[]
        for s in sti[0]:
            x.append(s)
        y_ini=0.5
        for j in range(0,4):
            y_ini+=x[j]*w[j]
        print sti,y_ini
        print
        b=b+a*(t-y_ini)
        for j in range(0,4):
            w[j]=w[j]+a*(t-y_ini)*x[j]
