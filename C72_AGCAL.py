r=range
for _ in[I:=input]*int(I()):
 t=I();L,o=len(t),0
 for i in r(1,L//2+1):
  if not L%i:
   x=[int(t[j:j+i]) for j in r(0,L,i)]
   if all(x[k]-x[~-k]==1 for k in r(1,len(x))):o=1;break
 print(o==1)