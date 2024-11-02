import textwrap

def wrap(string, max_width):
    result = ""
    slices = int(len(string)/max_width)
    st = 0
    end = max_width
    for sl in range(0,slices):
        part = string[st:end]
        part += '\n'
        st += max_width
        end += max_width
        result += part
    result += string[end-max_width:]
    
    return result

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width = 4
    result = wrap(string, max_width)
    print(result)