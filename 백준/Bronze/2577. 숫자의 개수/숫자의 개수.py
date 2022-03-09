a = int(input())
b = int(input())
c = int(input())

d = str(a*b*c)

for n in range(10): # 0-9
    num = str(n)
    print(d.count(num))
    