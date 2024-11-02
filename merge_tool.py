string = 'AABCAAADA'
k = 3
ss = []
for i in range(0,len(string)):
    if i % 3 == 0 and i+k < len(string):
        ss.append(string[i:i+k])
    elif i % 3 == 0 and i+k >= len(string):
        ss.append(string[i:])
vv = [dict.fromkeys(i) for i in ss]
cc = [''.join([k for k,v in t.items()]) for t in vv]
print(cc)