import math

a,b,v = map(int,input().split())
c = a - b
duration = math.ceil((v-b)/c)
print(duration)