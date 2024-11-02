# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n = 2#int(input())
a = [[1,2], [1,2]]
b = [[3,4], [3,4]]
# # for _ in range(0,n):
# #     a.append(list(map(int, input().split())))
# # for _ in range(0,n):
#     b.append(list(map(int, input().split())))
out = []
for i in range(0,len(a)):
    out.append(np.cross(np.array(a[i]), np.array(b[i])))

print(out)
    