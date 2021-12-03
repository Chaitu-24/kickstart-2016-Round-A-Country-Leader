def func(a):
    a=list(a)
    a=list(set(a))
    if " " in a:
        a.remove(" ")
    return len(a)
t=int(input())
for b in range(1,t+1):
    n=int(input())
    m=0
    ch=" "
    for i in range(n):
        a=input()
        if func(a)==m:
            if ch>a:
                ch=a
        elif func(a)>m:
            m=func(a)
            ch=a
    print("Case #{}: {}".format(b,ch))
