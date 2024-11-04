import re

def check_cc(number):
    #  It must start with a 4,5 or 6 --> ^[4,5,6]
    # 4 groups of sepearated by optional hyphen --> (?:-)?\d{4} --> optional hyphen,'?' repeated 0 or 1 time
    # specify the group length '{number}'
    # exclude repeated digits for 4 or more, ignoring hyphens --> (?!.*(\d)(?:-?\1){3})
    pattern = r'^(?!.*(\d)(?:-?\1){3})[4,5,6]\d{3}(?:-)?\d{4}(?:-)?\d{4}(?:-)?\d{4}$'
    if re.match(pattern, number):
        return True

    return False

check = list()
for _ in range(0, int(input())):
    cc_number = input()
    if check_cc(cc_number):
        check.append("Valid")
    else:
        check.append("Invalid")

print(*check, sep='\n')

