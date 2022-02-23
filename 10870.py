#피보나치
def getPivonachi(n):
    pivo = [0,1]
    for _ in range(n-1):
        pivo.append(pivo[-1]+pivo[-2])
#     print(pivo)
    return pivo[n]

n = int(input())

print(getPivonachi(n))