"""
아이디어
#최댓값이라고 했기 때문에 낮은 수부터 시작해야 한다.
#그 값을 딱 넘기 전까지가 그 개수이다
"""


S = int(input()) #100
res = 0
for i in range(1,S+1):
    val = i*(i+1)//2
    if val == S:
        res = S
    elif val > S:
        res = i-1
        break
print(res)