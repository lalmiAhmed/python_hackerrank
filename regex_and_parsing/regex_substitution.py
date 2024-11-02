import re


N = int(input("Enter the number of lines you want to appy the substitution to:\n"))
input_lines = []

for n in range(0,N):
    line = input()
    # (?<= ) positive lookbehind, (?= ) positive lookahead
    line = re.sub(r'(?<= )&&(?= )','and',line)
    line = re.sub(r'(?<= )\|\|(?= )','or',line)
    input_lines.append(line)

print(*input_lines, sep='\n')