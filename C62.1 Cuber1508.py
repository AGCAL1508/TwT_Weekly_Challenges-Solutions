for _ in[i:=input]*int(i()):
 s=i();a=0;c="";f = 0
 for n in range(len(s.split()[0])):
  if a >= int(s.split()[1]):a/=int(s[n-1]);break 
  else:
    if s[n].isalpha():a+=1;f=n+1
    else:a*=int(s[n])                    
 b=""
 for l in s[0:f]:
  try:b*=int(l)
  except:b+=l
 print(b[int(s.split()[1])%len(b)-1])