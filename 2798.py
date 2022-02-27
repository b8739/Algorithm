#블랙잭
from itertools import combinations

n,target = map(int,input().split())

nums = map(int,input().split()) 

max = 0

for i in combinations(nums,3):
    sum = 0
    for j in i:
        sum+=j
    if sum>max and sum<=target:
        max=sum
        
print (max)
