c=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
for _ in[i:=input]*int(i()):
 p=i().split()[0];m=i().split();a=list(map(int,m[::2]));b=list(map(int, m[1::2]))
 for d in c:
  if all(e in a for e in d):print(p);break
  if all(e in b for e in d):print(*(set(["X","O"])-set(p)));break
 else:print("Tie")