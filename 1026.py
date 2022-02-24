# 1026번

n = int(input())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

sorted_a = sorted(a_list, reverse=True)
sorted_b = sorted(b_list)

s = 0
for i in range(n):
    s += sorted_a[i] * sorted_b[i]

print(s)

"""풀이"""
"""
문제에서 제약을 주는 부분들이 있다.
1. 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
- 실제로 함수를 정의하란 말은 아님, 이 함수대로 적용해서 값을 도출하라는 말
2. 단, B에 있는 수는 재배열하면 안 된다.
- B는 재배열하면 안되지만 (sort), 재배열된 거를 새로운 변수로 만들어도됨 (sorted)
"""
