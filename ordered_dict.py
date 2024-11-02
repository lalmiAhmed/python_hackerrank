from collections import OrderedDict, defaultdict
N = int(input())
d = OrderedDict()
for _ in range(0, N):
    v= input().split()
    if ' '.join(v[:-1]) not in d.keys():
        d[' '.join(v[:-1])] = int(v[-1]) 
    else:
        d[' '.join(v[:-1])] += int(v[-1]) 
for e in d.items():
    print(*e, sep=' ')