N, M = map(int,input().split())
J = int(input())
start = 1
end = M
result = 0
for i in range(J):
    apple = int(input())
    if start<=apple<=end:
        continue
    else:
        if apple>end:
            move = apple-end
            end+=move
            start+=move
            result+=move
        elif start>apple:
            move = start-apple
            start-=move
            end-=move
            result+=move

print(result)