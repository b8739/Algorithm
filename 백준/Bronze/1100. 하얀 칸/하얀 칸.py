idx = 2
cnt = 0
for i in range(8):
    line = list(map(str,input()))
    #짝수일 때는 홀수가 흰색
    for j,k in enumerate(line):
        #홀수칸이고 흰색에 말이 있으면 +1
        if idx % 2 ==0 and j % 2 == 0 and k == 'F':
            cnt+=1
        elif idx % 2 !=0 and j % 2 != 0 and k == 'F':
            cnt+=1
    idx+=1
print(cnt)