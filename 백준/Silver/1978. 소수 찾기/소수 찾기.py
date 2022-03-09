test = int(input())

num = list(map(int,input().split()))
minus = 0
for n in num: #[1,2,35]
    if n<2:
        minus+=1
        continue
    for i in range(2,n):
        if n % i == 0:
            minus+=1
            break
print(len(num)-minus)