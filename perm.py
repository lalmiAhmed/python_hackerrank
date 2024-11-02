from itertools import permutations
inp = (input()).split()
string = inp[0]; k = int(inp[1])
print(*sorted([''.join(list(l)) for l in list(permutations(string, k))]), sep='\n')
