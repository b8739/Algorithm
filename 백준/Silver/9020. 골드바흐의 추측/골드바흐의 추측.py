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




    