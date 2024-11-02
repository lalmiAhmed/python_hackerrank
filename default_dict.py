# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

positions = defaultdict(list)

n, m = map(int,input().split())
for pos in range(1,n+1):
    positions[input()].append(pos)
res = []
for _ in range(m):
    res.append(positions.get(input(), [-1]))
for li in res:
    print(*li,sep=' ')


   