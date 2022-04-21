n = int(input())

for i in range(n):
    s = list(map(str,input().split()))

    for j in range(len(s)):
        print(s[j][::-1],end=' ')
    print()