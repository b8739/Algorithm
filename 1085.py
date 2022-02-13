p = []
x,y,w,h = map(int, input().split())

p.append(abs(0 - x))
p.append(abs(x - w))
p.append(abs(0 - y))
p.append(abs(y - h))

print(min(p))
