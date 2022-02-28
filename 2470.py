# 2470번 두 용액

#가장 작은 값을 찾아서 0이 되려면 얼마나 더해줘야하는지
n = int(input())
nums = list(map(int,input().split()))

nums.sort()

extra = 0

if nums[0] < 0:
    extra = abs(min(nums))
    for idx in range(n):
        nums[idx]+=extra

start = 0
end = len(nums)-1
d = 2000000001
res = []

for idx in nums:
    if end == start:
        break
    sum = nums[end]+nums[start]-(extra*2)
    if abs(0-d)>abs(sum):
        d = sum 
        res = [nums[start]-extra,nums[end]-extra]
    if(sum<0):
        start+=1
    elif(sum>0):
        end-=1
    else :# 0인 경우
        res = [nums[start]-extra,nums[end]-extra]
        break

for i in res:
    print(i,end=' ')