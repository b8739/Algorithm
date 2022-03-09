n = int(input())
r = []

for _ in range(n):
    r.append(int(input()))

r.sort()

final = []

for i in r:
    final.append(i*n)
    n-=1

print(max(final))