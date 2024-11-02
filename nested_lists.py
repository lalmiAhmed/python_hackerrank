if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    mini = min([r[1] for r in records])
    new = []
    for r in records:
        if r[1] != mini:
            new.append(r)
    mini = min([r[1] for r in new])
    out = []
    for r in new:
        if r[1] == mini:
            out.append(r[0])
    
    print(mini)  
    print(records)
    print(sorted(out))
