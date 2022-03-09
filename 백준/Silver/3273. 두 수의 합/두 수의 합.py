n = int(input())
nums = list(map(int,input().split())) 
target = int(input())
nums.sort()

s = 0
e = len(nums)-1

cnt = 0

#만약 x면 end -=1, start+=1
#만약 x보다 크면 end -=1
#만약 x보다 작으면 start=+1
while e>s:
    sum = nums[s]+nums[e]
    if sum==target:
        cnt+=1
        e-=1
    elif sum>target:
        e -=1
    elif sum<target:
        s+=1
print(cnt)