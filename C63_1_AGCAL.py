for _ in[i:=input]*int(i()):
 n=i().split("||");l=[];s=n[1].replace(" ","").split(",")
 for _ in range(int(n[0])):
  b=i().split(":");a=b[0].replace(" ", "").split(",");t=[]
  if len(a)==len(s):
   for c in s:
    if c == "?":t.append(True)
    else:t.append(c == a[s.index(c)])
   if all(t):l.append(b[1].strip()) 
 print(", ".join(l))