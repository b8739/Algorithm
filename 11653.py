#11653번 소수 구하기
num = int(input()) #72

primes = []

def primeFac(num):
    if num < 2:
        return []
    
    isPrime = True
    
    for n in range(2,num):
        if num%n == 0:
            primes.append(n)
            isPrime = False
            primeFac(num//n)
            break;
    
    if isPrime == True:
        primes.append(num)
    
    return primes

for p in primeFac(num):
    print(p)
