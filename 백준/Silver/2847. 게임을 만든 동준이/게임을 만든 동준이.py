#sort 역순으로
#0부터 해서 다음꺼가 이전꺼보다 크다면 count에 <큰거-작은거+1>만큼 증가시킨다
#만약 작다면 다음으로 넘어간다

N = int(input())

S = [int(input()) for _ in range (N)]

S = S[::-1]
# 아래와 같이 하면 안됨...
# S = sort(reverse=True) 

count = 0
for i in range(N-1):
    if S[i] <= S[i+1]:
        subtract = S[i+1]-S[i]+1
        S[i+1]-= subtract
        count += subtract
    else:
        continue
print(count)