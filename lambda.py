cube = lambda x: x*3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    o = [0, 1]
    while(len(o) < n):
        o.append(o[-1]+o[-2])
    return o[:n]
if __name__ == '__main__':
    n = int(input())
    print(cube(fibonacci(n)))
    # print(list(map(cube, fibonacci(n))))