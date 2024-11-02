# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = list(map(int, input().split()))
poly = input().split()
def mat(op1, op2, op):
    if op == '+':
        return int(op1) + int(op2)
    elif op == '-':
        return int(op1) - int(op2)
    elif op == '*':
        return int(op1) * int(op2)
    elif op == '/':
        return int(op1) / int(op2)

operands = []
operations = []
res = 0
for i in range(0, len(poly)):
    stack = 0
    coef = 1
    if i%2==0:
        tmp = list(poly[i]).copy()
        if '*' in tmp:
            tmp.remove('*')
        if poly[i].count('*') == 3: #case of coef*x**p
            coef = int(poly[i][:poly[i].index('*')])
            stack = int(x**int(poly[i][tmp.index('*')+3:]))
        elif poly[i].count('*') == 2: #case of x**p
            stack = int(x**int(poly[i][poly[i].index('*')+2:]))
        elif poly[i].count('*') == 1: #case of coef*x
            coef = int(poly[i][:poly[i].index('*')])
            stack = x
        elif poly[i] == 'x': #case of x
            stack = x
        else: #case of coef
            stack = int(poly[i])
        stack = coef * stack
        operands.append(stack)
    else:
        operations.append(poly[i])
if len(operands) > 1:
    res = mat(operands[0], operands[1], operations[0])
    for i in range(1, len(operations)):
        res = mat(res, operands[i+1] ,operations[i])
else:
    res = operands[0]
        
if res == k:
    print(True)
else:
    print(False)
