from collections import namedtuple
N = int(input())
student  = namedtuple('student', input())
sum = 0
for i in range(0,N):
    tmp = student(*list(input().split()))
    sum += int(tmp.MARKS)
print(round(sum/N, 2))
