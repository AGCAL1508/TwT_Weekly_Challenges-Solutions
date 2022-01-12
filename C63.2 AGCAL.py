for _ in[i:=input]*int(i()):
 a,k=i().split();d=0;s=[a[l:j]for l in range(len(a))for j in range(l+1,len(a)+1)]
 for b in s:
  db={}
  for h in b:
   db[h]=db.get(h,0)+1
  if len([db[y]for y in db if db[y]>=int(k)])==len(db):
   if len(b)>d:d=len(b)
 print(d)