for _ in[i:=input]*int(i()):
    n=int(i());a=i().split();b=i().split()
    a.append(a[0])
    b.append(b[0])
    for d in range(len(a)-1):
        g=False
        p1a=list(map(int,a[d].split(",")))
        p2a=list(map(int,a[d+1].split(",")))
        for e in range(len(b)-1):
            p1b=list(map(int,b[e].split(",")))
            p2b=list(map(int,b[e+1].split(",")))
            if (p1a[0] < min([p1b[0],p1b[0]]) and p2a[0] > max([p1b[0],p1b[0]])) or (p2a[0] < min([p1b[0],p1b[0]]) and p1a[0] > max([p1b[0],p1b[0]])):
                if (max([p1b[0],p1b[0]]) < p1a[1] > 0 and p2a[1] <= max([p1b[0],p1b[0]])) or (p2a[1] > min([p1b[0],p1b[0]]) and p1a[1] <= max([p1b[0],p1b[0]])):
                    g=True
                    break
        if g:break
    print(str(g).lower())
# It doesn't pass all the test cases, but idc anymore
# for _ in[i:=input]*int(i()):
#     i();a=i().split();b=i().split()
#     for c in range(len(a)):
#         temp_bool=False
#         p1a=a[c].split(",")
#         try:
#             p2a=a[c+1].split(",")
#         except:p2a=a[0].split(",")
#         ap=list(map(int,[p1a[0],p2a[0]]))
#         ar=range(min(ap),max(ap))
#         bp=list(map(int,[p1a[1],p2a[1]]))
#         br=range(min(bp),max(bp))
#         for d in range(len(b)):
#             p1b=b[d].split(",")
#             try:p2b=b[d+1].split(",")
#             except:p2b=b[0].split(",")
#             bp2=list(map(int,[p1b[0],p2b[0]]))
#             br2=range(min(bp2),max(bp2))
#             bp3=list(map(int,[p1b[1],p2b[1]]))
#             br3=range(min(bp3),max(bp3))
#             if any([int(p1b[0]) in ar, int(p2b[0]) in ar]) or set(br2).issubset(ar) and len(br2)>0:
#                 if any([int(p1b[1]) in br, int(p2b[1]) in br]) or set(br3).issubset(br) and len(br3)>0:
#                     temp_bool=True
#                     break
#         if temp_bool:break
#     print(str(temp_bool).lower())