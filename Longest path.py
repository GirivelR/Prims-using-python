from collections import defaultdict
n=int(input('Enter the number of vertices: '))+1
d=defaultdict(list)
for i in range(n):
    d[int(input())].append(int(input()))
print(d)
l=v=[0]*n
m=c=0
