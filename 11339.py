# 11339 ATM

#내가 짠 코드
n = int(input())
p = list(map(int,input().split()))

sum = 0
p.sort()

last = p.pop()
idx = len(p)+1

for i in p: # 1 2 3 3 
    sum+=i*idx
    idx-=1
    
print(sum+last)



#다른 사람이 짠 코드 

n = int(input()) # 사람 수 
arr = list(map(int,input().split())) # 인출 시간
arr.sort() # 정렬

result = 0

for i in range(1,n):
    arr[i] += arr[i-1] # 인출 시간 갱신

print(sum(arr))



#다른 사람이 짠 코드 (중첩 반복문 사용)
n = int(input())
s = list(map(int, input().split()))

num = 0
s.sort()

for i in range(n):
    for j in range(i + 1):
        num += s[j]

print(num)