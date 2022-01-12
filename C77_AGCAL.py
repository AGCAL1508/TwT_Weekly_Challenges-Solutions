def a(b):
 c="1126422428"
 if b<10:return int(c[b])
 return([4,6][((b//10)%10)%2==0]*a(b//5)*int(c[b%10]))%10
for _ in[i:=input]*int(i()):print(a(int(i())))