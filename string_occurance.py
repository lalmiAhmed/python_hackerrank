i = "ABCDCDC"
f = "CDC"
t_len = len(f)
counter = 0
ind = 0
for t_len in range(t_len, len(i)+1):
    comp = i[ind:t_len]
    ind +=1
    if comp == f:
        counter +=1
print(counter)
