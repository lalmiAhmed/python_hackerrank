if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(0,N):
        cmd = input().split(' ')
        if 'insert' in cmd:
            arr.insert(int(cmd[1]), int(cmd[2])) 
        elif cmd[0] == "print":
            print(arr)
        elif 'remove' in cmd:
            arr.remove(int(cmd[1]))
        elif 'append' in cmd:
            arr.append(int(cmd[1]))
        elif cmd[0] == "sort":
            arr = sorted(arr)
        elif cmd[0] == "pop":
            arr.pop()
        elif cmd[0] == "reverse":
            arr.reverse()
        else:
            print("command not recognized")
