n = int(input())
v = list(input() for _ in range(n))

word = list(v[0])
length = len(word)

start = 0

for i in range(1,n):
    for j in range(length):
        if word[j] != v[i][j]:
            word[j] = '?'
            continue
print("".join(word))
            
# 3
# config.sys
# config.inf
# configures