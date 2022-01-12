a=dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)
for _ in[i:=input]*int(i()):f=i()+' ';print(f);u=[a[c]for c in f];print(sum([-u[k],u[k]][u[k]>=u[k+1]]for k in range(len(u)-2)))