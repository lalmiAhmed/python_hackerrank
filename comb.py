from itertools import combinations
inp = (input()).split()
string = inp[0]; k = int(inp[1])
for i in range(1,k+1):
    print(*sorted([''.join(sorted(l)) for l in list(combinations(string, i))]), sep='\n')

