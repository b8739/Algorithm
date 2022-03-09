up,down = map(int,input().split())

def primeSieve(up,down):
    sieve = [False,False] + [True]* (down-1)
    
    m = int(down**0.5)
    
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,down+1,i):                
                sieve[j] = False
                
    primes = [idx for idx,s in enumerate(sieve) if s == True if idx >= up]

    return primes

for p in primeSieve(up,down):
    print (p)
    