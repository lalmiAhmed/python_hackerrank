
import re
patt = r"[\w :,]+(#(?:[a-fA-F0-9]{3}|[a-fA-F0-9]{6}))\b"
count = 0
colors = dict()
for _ in range(0, int(input())):
    line = input()
    if re.search(patt, line):
        colors[count] = re.findall(patt, line)
        count +=1
# print(colors)
for k,v in colors.items():
    print(*v, sep='\n')