from itertools import permutations
n = int(input())
k = int(input())
s = []

for _ in range(n):
    s.append(input())

permute = list(permutations(s,k))
result = []

for i in permute:
    result.append("".join(list(i)))

print(len(set(result)))