def isPrime(num):
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
    

up = int(input()) #60
down = int(input()) #100
primes = list()

for num in range(up, down+1):
    if isPrime(num):
        primes.append(num)
        
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
