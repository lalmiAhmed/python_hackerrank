def print_rangoli(size):
    # your code goes here
    alpha = [chr(i) for i in range(97,123)]
    ref = alpha[:size]
    center = list(reversed(ref))+ref[1:]
    content = []
    for l in range(0, size):
        content.append(list(reversed(ref[l:]))+ref[l+1:])
    if size >1:
        print(*['-'.join(e).center(len(center)*2-1, '-') for e in reversed(content[1:])], sep='\n')
    print('-'.join(center))
    if size >1:
        print(*['-'.join(e).center(len(center)*2-1, '-') for e in content[1:]], sep='\n')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)