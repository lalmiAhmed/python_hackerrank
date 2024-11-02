from collections import Counter

#shoes = [2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
num_shoes = int(input())
shoes = [int(i) for i in input().split()]


print(Counter(shoes))
