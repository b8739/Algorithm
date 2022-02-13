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
    candidate = []
    #하나씩 감소하면서, 자신보다 작으면서 가장 근접한 소수 찾기
    for n in range(even,1,-1):
        if primes[n] and primes[even-n]:
            #비어있으면 아직 못 찾은거니 넣음
            if not candidate:
                candidate = [n, even-n]
            #이미 존재한다면, 비교해서 차가 작은 값을 넣음
            else:
                a = abs(candidate[0]-candidate[1])
                b = abs(n-(even-n))
                if a>b: 
                    candidate[0] = n
                    candidate[1] = even-n
    candidate.sort();

    print (f'{candidate[0]} {candidate[1]}')
    return     
        
#짝수

primes = primeSieve(10000)

# print(primes)
# primes.reverse()

test = int(input())

for t in range(test):
    getGoldBach()




    