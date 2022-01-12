for _ in [i:=input]*int(i()):
    w,t = i(),i();wl=[];tl=[];a =""
    if set(w) == set(t):
        for l in range(len(w)):
            if a=="":a=w[l]
            else:pass
            try:
                if w[l]==w[l+1]:a+=w[l+1]
                else:wl.append(a);a =""
            except:
                if w[l]==w[l-1]:a+=w[l];wl.append(a)
                else:wl.append(a)
                a=""
        for l in range(len(t)):
            if a=="":a=t[l]
            else:pass
            try:
                if t[l]==t[l+1]:a+=t[l+1]
                else:tl.append(a);a =""
            except:
                if t[l]==t[l-1]:a+=t[l];tl.append(a)
                else:tl.append(a)
        if len(tl) != len(wl):
            print('no')
        else:
            a=False
            for l in range(len(tl)):
                if len(tl[l]) >= len(wl[l]):
                    pass
                else:
                    a=True
            if a:
                print("no")
            else:
                a=""
                for c in w:
                    if c in a:pass
                    else:a+=c
                b=""
                for c in t:
                    if c in b:pass
                    else:b+=c
                if a==b:print("yes")
                else:print("no")
    else:
        print("no")