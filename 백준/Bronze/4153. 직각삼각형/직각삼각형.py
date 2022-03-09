while True:
    nums = list(map(int,input().split()))
    if nums.count(0) == 3:
        break        
        
    max_num = nums.pop(nums.index(max(nums)))
    
    if max_num**2 == (nums[0]**2 + nums[1]**2):
        print('right')
    else:
        print('wrong')
    