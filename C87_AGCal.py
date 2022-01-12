def a(n,c):
    l=[]
    while n>c:
        try:
            l.append(n%c)
            n=n//c
        except:
            print("yes")
            break
    else:
        l.append(1)
    print("end")
    return l
for _ in[i:=input]*int(i()):
    f=int(i())
    d=0
    for i in range(36):
        if set(a(f,i))=={1}:
            d+=1
    print("end")
    print(d)
