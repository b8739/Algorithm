def primeSieve(num):
    sieve = [False,False] + [True]* (num-1)
    
    m = int(num**0.5)
    
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,num+1,i):                
                sieve[j] = False
            
    return sieve

def getGoldBach():
    # 짝수 받기
    even = int(input()) #10 
    #하나씩 감소하면서, 자신보다 작으면서 가장 근접한 소수 찾기
    for n in range(even//2,1,-1): 
        if sieve[n] and sieve[even-n]:
            print (f'{n} {even-n}')
            break
    return     

sieve = primeSieve(10000)

test = int(input())

for t in range(test):
    getGoldBach()

#변경사항
#23번줄: t를 돌때마다 채를 찾는게 아니라 primeSieve로 미리 구함
#17번줄: 두 소수의 차이가 가장 작은것을 출력하여야 하고, 작은 소수부터 출력을 하기 때문에 짝수를 2로 나눈 몫부터 시작한다. 두 소수를 찾으면 break.




    