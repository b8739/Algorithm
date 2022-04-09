word = input()

S = [0]*26

# ord:알파벳을 넣으면 숫자
# chr:숫자를 넣으면 알파벳

for i in word:
    S[ord(i)-65] += 1

odd_cnt = 0
result = ''
odds = ''
for i,v in enumerate(S):
    if v == 0:
        continue 
    #짝수
    if  v % 2 ==0:
        result += (chr(i+65)*(v//2))
    #홀수
    else:
        result += (chr(i+65)*(v//2))
        odds = chr(i+65)
        odd_cnt+=1
    #끝나는 조건
    if odd_cnt > 1:
        break
    
# result.sort()

if odd_cnt > 1:
    print ("I'm Sorry Hansoo")
else:
    print(result+odds+result[::-1])

