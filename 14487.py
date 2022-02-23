# 14487번 욱제는 효도쟁이야! 
# 수정 전
t = int(input())
distance = list(map(int,input().split()))
sum = 0
maxValue = max(distance)

for d in distance:
    if d != maxValue:
        sum+=d
        
print(sum)

# 수정 후
n = int(input())
nums = list(map(int, input().split()))
print(sum(nums) - max(nums))

#틀린 이유
#max인 거리가 여러개라면 그 값은 안 더해짐
#그리고 코드를 훨씬 짧게 할 수 있는데 거기까지 생각 안 함
        
    