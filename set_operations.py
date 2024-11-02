# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
my_set = set([int(i) for i in input().split()])
n_cmd = int(input())
for _ in range(0, n_cmd):
    cmd = input().split()
    if cmd[0] == "pop":
        my_set.pop()
    elif cmd[0] == "discard":
        my_set.discard(int(cmd[1]))
    elif cmd[0] == "remove":
        if int(cmd[1]) in my_set:
            my_set.remove(int(cmd[1]))
    else:
        pass
print (sum(list(my_set)))