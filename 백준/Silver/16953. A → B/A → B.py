#경우의 수
#뒤에 1만 붙이면 그 값이 되는경우
#1을 붙이고 2를 곱해줘야 하는 경우
#1을 붙이고 2를 곱해주고 다시 1을 붙이는 경우

#만약 B뒤에 1이 있으면 1을 뺴고 그 값이 되는 순간 까지를차즌ㄴ다
#아니면 뒤에 1이 나올때까지 2로 나눈다.

a,b = map(int,input().split())
cnt=1

while b!=a:
#while 끝내는 조건
    if a>b:
        cnt = -1
        break
    if b%10 == 1:
        b//=10
        cnt+=1
    else:
        if b%2==0:
            b//=2
            cnt+=1
        else:
            cnt = -1
            break
print(cnt)
