for _ in[i:=input]*int(i()):y,x=i().split();b=[];a=[i().split()for _ in range(int(y))];[b.append(a[c][d:d+2]+a[c+1][d:d+2])for c in range(int(y)-1)for d in range(int(x)-1)if a[c][d:d+2]+a[c+1][d:d+2]not in b];print(len(b))