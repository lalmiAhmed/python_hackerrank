from itertools import combinations_with_replacement as rp
inp = (input()).split()
string = inp[0]; k = int(inp[1])
print(*sorted([''.join(sorted(l)) for l in list(rp(string, k))]), sep='\n')

