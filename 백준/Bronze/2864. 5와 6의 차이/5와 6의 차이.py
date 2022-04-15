A,B = map(str,input().split())

A = A.replace('6','5')
B = B.replace('6','5')

print(int(A)+int(B))

A = A.replace('5','6')
B = B.replace('5','6')

print(int(A)+int(B))
