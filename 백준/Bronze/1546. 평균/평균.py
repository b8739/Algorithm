sub_num = int(input()) # 3

before_score = list(map(int,input().split()))
after_score = []

max_score = 0

max_score = max(before_score)

for n in before_score:
    after_score.append(n/max_score)
    
print((sum(after_score)/(sub_num)*100))
    