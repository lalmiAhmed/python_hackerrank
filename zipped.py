# Enter your code here. Read input from STDIN. Print output to STDOUT
n , x= list(map(int, input().split()))
tot = []
for _ in range(0, x):
    tot.append(list(map(float, input().split())))
print(*[[round(sum(el)/len(el), 1) for el in zip(*tot)]], sep='\n')
