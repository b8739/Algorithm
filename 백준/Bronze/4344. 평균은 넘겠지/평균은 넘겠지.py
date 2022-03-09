n = int(input())

for _ in range(n):
    nums = list(map(int,input().split()))
    num_students = nums[0]
    
    total = sum(nums[1:])
    avg = total//num_students
    
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt+=1
    rate = round((cnt/num_students)*100,3)
    print(f'{rate:.3f}%')