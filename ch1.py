if __name__ == '__main__':
    n = int(input())
    if n >= 1 and n <= 150:
        r = 1
        out = 1
        for i in range(1,n):
            if i<=8:
                r += 10**i
                out += r
            if i>8:
                print("more than 10")
                r += 10**(i+1)
                out += r+10
    print(out)
    print(r)
