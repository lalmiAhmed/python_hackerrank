n, m = input().split()
n = int(n); m = int(m)
lines = ["|"]
ref = [lines.copy()]
for l in range(0,int(n/2)):
    print(("."+'..'.join(lines)+".").center(m, '-')) 
    lines += ["|", "|"]
    ref.append(lines.copy())
print("WELCOME".center(m, '-'))
print(*[("."+'..'.join(l)+".").center(m, '-') for l in reversed(ref[:-1])], sep="\n")

