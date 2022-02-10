
def countPrime(num): #10
    limit = num * 2
    
    sieve = [False, False] + [True] * (limit-1)
    

    m = int(limit**0.5)
    
    for i in range(2,m+1):
        if sieve[i] == True:    
            for j in range(i+i, limit+1 ,i):
                sieve[j] = False

    prime = [idx for idx,s in enumerate(sieve) if s == True if num<idx<=limit]

    return len(prime)

n = 1

while True:
    n = int(input())
    if n == 0:
        break
    print(countPrime(n))

