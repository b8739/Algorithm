import sys
input = sys.stdin.readline
n = int(input())
s = []
for _ in range(n):
    cmd = input().split()
    if len(cmd)==2:
        s.append(cmd[1])
    elif cmd[0] == 'pop':
        if not s:
            print(-1)
        else: 
            print(s.pop())
    elif cmd[0] == 'size':
        print(len(s))
    elif cmd[0] == 'empty':
        if not s:
            print(1)
        else: print(0)
    elif cmd[0] == 'top':
        if not s:
            print(-1)
        else:
            print(s[-1])

# 7
# pop
# top
# push 123
# top
# pop
# top
# pop