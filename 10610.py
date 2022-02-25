# 10610번 30
"""
아이디어
#30의 배수 중 가장 큰 수
#string: 재배열 가능
#순서를 고려한 조합: 순열
#순열로 찾아보고 30으로 나누었을때 나머지가 0이라면 기록한다.
#그중 가장 큰 값을 반환한다
"""

#실패: 메모리 초과
from itertools import permutations
n = input()
res = 0

for i in list(permutations(n,len(n))):
    sum = ''

    for j in i:
        sum+=j

    if int(sum) % 30 == 0:
        if res < int(sum):
            res = int(sum)
if res == 0:
    print (-1)
else:
    print(res)
    
"""
풀이
이 문제는 해당 수가 3의 배수임을 알기 위한 공식을 알아야 풀 수 있다.

해당 수의 모든 자릿수의 합이 3의 배수가 되면 된다.

또한, 3이 아닌 30의 배수이므로 숫자 내에 0이 없다면 -1을 출력해야 한다.

 

받은 숫자 내에 0이 없다면 -1 출력
숫자들의 합이 3으로 나누어 떨어지지 않는다면 -1 출력
걸러진 수를 내림차순으로 정렬 (언제 해도 상관은 없음)
"""
n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))