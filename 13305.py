#13305 주유소
"""
두번째 짠 코드 (58점) 
오답 요인
1) 미리 기록했던 값과 반복문에서 새로 나오는 값을 비교하면 됐는데,굳이 findCheaper라는 함수로 구현하려고 해서 시간 지연
    - 어차피 모든 값을 반복문을 돌기 때문에, 굳이 자기보다 작은 값을 미리 구해놓을 필요 없음
2) 함수에서 global variable에 접근하고자 한다면 앞에 global이라고 붙여야 함, 이거를 몰라서 시간 지연
"""
city = int(input()) #4
distance = list(map(int,input().split())) #3,2,1
prices = list(map(int,input().split())) #6,9,7,5

prices.pop()

current_p = prices[0]
cheaper_p = 0

#자기보다 작은 걸 찾는 과정

def findCheaper(idx): 
    global current_p
    global cheaper_p
    
    for i in prices[idx:]:
        if current_p>i:
            cheaper_p = i
            break       
    return 

sum = 0

findCheaper(1)

for idx,i in enumerate(prices):

    if i == cheaper_p:
        current_p = i
        findCheaper(idx)

    sum += current_p*distance[idx]
    
print(sum)
        
"""두번째 짠 코드 (100점)"""
city = int(input()) #4
distance = list(map(int,input().split())) #3,2,1
prices = list(map(int,input().split())) #6,9,7,5

prices.pop()

#처음꺼는 끝
current_p = prices[0]
idx = 1
sum = current_p*distance[0]

for i in prices[1:]:
    if current_p>i:
        current_p = i
    sum += current_p*distance[idx]
    idx += 1
    
print(sum)
        