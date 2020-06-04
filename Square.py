for _ in range(int(input())):
    x,y=[],[]
    for i in range(int(input())):
        a,b=map(int,input().split())
        x.append(a)
        y.append(b)
    a=abs(min(x)-max(x))
    b=abs(min(y)-max(y))
    print(max(a,b)**2)
