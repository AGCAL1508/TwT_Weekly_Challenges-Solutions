for _ in[i:=input]*int(i()):
 a=i().split();b=a.copy();c=0;e=1;l=0;t=0
 while 1:
  l=a.copy();e=int(b[c]);a[c]="#";c=((c+e)%len(a))
  if l==a:t+=1
  if set(a)=={'#'}or t==2:break
 print((set(a)=={'#'}or len(a)==1)and c==0and not['0']==b)