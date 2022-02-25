"""
아이디어
-를 기준으로 split으로 수식을 나눈다.
"""


#틀림
e = input().split('-') 

final = ''

for i in e:
    while i[0] == '0':
        i = i[1:]
    final += '('+ i + ')'+ '-'

final = final[:-1]
# print(final)
print(eval(final))

"""
오답풀이
테스트 케이스로 00009-000008+00007를 넣어보고서야 틀린거를 알았다. (다른 거는 다 맞게 나옴)
'-'를 기준으로 나누었기 때문에 수식이 (9)-(8+00007) 이렇게 나눠지게 된다.
결론적으로 eval을 써서 해결하려고 하면 참 귀찮게 된다.

"""

#다른 사람 풀이

a = input().split('-')

res = 0

for i in a[0].split('+'):
    res += int(i)

for i in a[1:]:
    for j in i.split('+'):
        res -= int(j)
        
print(res)

"""
정답 헤설
첫번째 수를 제외한 나머지를 전부 첫번째에서 빼야 한다는 점을 활용해서 푸는 방식이다.
"""