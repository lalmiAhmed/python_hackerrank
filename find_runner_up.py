if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())
    n = 5
    arr = [2, 3, 6, 6, 5]
    arr = list(set(arr))
    arr.remove(max(arr))
    print(max(arr))
    #runner_up = max(arr)
    #print(runner_up)
