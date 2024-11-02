def wrapper(f):
    def fun(l):
        # complete the function
        ll = list()
        for num in l:
            if len(num) > 10:
                if num[0] == "+":
                    ll.append("+91 "+num[3:8] + " " + num[8:])
                elif num[0] == "0":
                    ll.append("+91 "+num[1:6] + " " + num[6:])
                else:
                    ll.append("+91 "+num[2:7] + " " + num[7:])
            else:
                ll.append("+91 "+num[:5] + " " + num[5:])
        val = f(ll)
        return val
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 