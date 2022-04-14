A,B = map(int,input().split())
N = int(input())
result = abs(A-B)

channel = []
for i in range(N):
    result = min(result,abs(B - int(input()))+1)

print(result)