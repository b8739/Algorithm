from itertools import permutations

n = int(input())
#덧셈, 뺄샘, 곱셈, 나눗셈

#최댓값
# 1이면 더하는게 좋고, 부호가 같으면 곱하는게 좋음

v = list(map(int,input().split()))
cmd = list(map(int,input().split()))
new_cmd = []
cmd_type = ['+','-','*','//']

for idx,i in enumerate(cmd):
    for _ in range(i):
        new_cmd.append(cmd_type[idx])

answer = []
p = list(set(permutations(new_cmd, n-1)))  # 순열
for i in p: #p:[('+,+,-'),('+,+,-')]
    num = v[0]
    for j in range(n-1):
        if i[j] == '+':
            num+=v[j+1]
        elif i[j] == '-':
            num-=v[j+1]
        elif i[j] == '*':
            num*=v[j+1]
        else:
            if num//v[j+1] <0:
                num = -(-num//v[j+1])
            else:
                num = num//v[j+1]
    answer.append(num)
    
print(max(answer))
print(min(answer))