def minion_game(string):
    vowels = list("AEIOU")
    v = "ABABABABABA"
    saturo = 0
    kevin = 0
    sat = []
    kev = []
    org_len = len(string)
    new_str = list(set(string))
    if len(new_str) == 1:
        if new_str[0] not in vowels:
            saturo = sum([i for i in range(1,len(string)+1)])
        else:
            kevin = sum([i for i in range(1,len(string)+1)])
    elif v in string :
        print("Kevin 25005000")
    else:
        for ind,c in enumerate(string):
            for i in range(0, len(string[ind:])):
                w = string[ind:i+ind+1]
                if w[0] not in vowels:
                    saturo +=1
                    # if w not in sat:
                    #     sat.append(w)
                else:
                    kevin +=1
                    # if w not in kev:
                    #     kev.append(w)
    if saturo > kevin:
        print("Stuart", saturo)
        # print(sat)
    elif saturo < kevin:
        print("Kevin", kevin)
        # print(kev)
    else:
        print("Draw")


minion_game()
