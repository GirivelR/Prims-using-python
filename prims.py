n=int(input('Enter the number of vertices: '))
d={}
for i in range(n):
    d[i]=[]
    print('Enter the values for ',str(i))
    for j in range(n):
        d[i].append(int(input()))
ver=[0]*n
p=[None]*n
key=[9999]*n
key[0]=0
for i in range(n):
    m=9999
    for j in range(n):
        if key[j]<m and ver[j]==0:
            m=key[j]
            u=j
    ver[u]=1
    for j in range(n):
        if d[u][j]>0 and ver[j]== 0 and key[j]>d[u][j]:
            key[j]=d[u][j]
            p[j]=u
for i in range(1,n):
    print(p[i],'-',i,' ',d[i][p[i]])
