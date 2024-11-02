def swap_case(s):
    r = ""
    #for l in s:
        #if l.isupper():
            #r += l.lower()
        #else:
            #r += l.upper()
    r = ''.join([l.lower() if l.isupper() else l.upper() for l in s])
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
