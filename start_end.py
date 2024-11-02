import re
S, k = input(), input()
matches = re.finditer(f'(?=({k}))', S)
indexes = lambda m: (m.start(1), m.end(1) - 1)
results = [*map(indexes, matches)] or [(-1, -1)]

print(*results, sep='\n')