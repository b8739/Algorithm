import sys
input = sys.stdin.readline
N = int(input())

prediction = [int(input()) for _ in range(N)]
prediction.sort()

result = 0

for i in range(1,N+1):
    result += abs(prediction[i-1]-i)

print(result)