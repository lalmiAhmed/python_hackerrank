import re
patt = r"[789][\d]{9}\b"
for _ in range(0, int(input())):
    num = input()
    if bool(re.match(patt, num)):
        print("YES")
    else:
        print("NO")