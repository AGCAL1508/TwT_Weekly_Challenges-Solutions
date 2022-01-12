def a(b):return b if len(str(b))==1 else a(str(sum(map(int,b[::1]))))
for i in[i:=input]*int(i()):print(a(i()))