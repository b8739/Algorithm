#10162 전자레인지

#수정 전
t = int(input()) #ex.321

def btnCounter(t):
    five_m = 0 #5분 = 300초
    one_m = 0 #1분 = 60초
    ten_s = 0 #10초
    #안 나눠떨어지는 경우
    if t%10 !=0:
        return -1
    if t>300:
        five_m = t//300 
        t %= 300 
    if t>60:
        one_m = t//60
        t %= 60
    if t>10:
        ten_s = t//10
        t %= 10
    return '%d %d %d' %(five_m,one_m,ten_s)

print(btnCounter(t))

#수정 후
T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    A = T // 300
    B = (T % 300) // 60
    C = (T % 300) % 60 // 10
    print(A, B, C)

#틀린 이유 
#'수정 전'에서 if문으로 t가 해당 숫자보다 클 때만 (ex. t>300) 고려했기 때문에, 딱 맞아떨어지는 300,60,10이 나오면 if를 안 거치게 되는 문제 발생
# 그리고 if를 안넣어도 어차피 순차적으로 위에서부터 아래로 거치게 되는데 쓸데없이 if를 사용해서 코드를 길어지게 만듦