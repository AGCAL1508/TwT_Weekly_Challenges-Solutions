i=input
for _ in" "*int(i()):
    h,d,f,s,n,l=i(),i(),i(),i(),0,[]
    for y in [f,s]:
        for j,b in enumerate(range(int(h)//2)):

            if y[j]=="1":l+=[[[f,s].index(y),b]]
    try:
        if f.index("2")==-1:e=s.index("2")
        else:e=f.index("2")  
        t=1;dt=0
        for q in l:
            if abs((q[1]+q[0])-e)<t:
                t=abs((q[1]+q[0])-e)
        print(t)
    except:
        print(0)