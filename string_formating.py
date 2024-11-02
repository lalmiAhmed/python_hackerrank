def print_formatted(number):
    # your code goes here
    n_t = len(bin(number)[2:])
    if n_t > 2:
        ss = ""
    else:
        ss = " "
    for _ in range(1,n_t):
        ss += " "
    if number > 63:
        vv = ss[0:-1]
    else:
        vv = ss
    
    for n in range(1, number+1):
        print(ss[:-1] + str(n).rjust(len(str(number))) + vv + str(oct(n)[2:]).rjust(len(oct(number)[2:])) + ss + str((hex(n)[2:]).upper()).rjust(len(hex(number)[2:])) + " " + bin(n)[2:].rjust(len(bin(number)[2:])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)