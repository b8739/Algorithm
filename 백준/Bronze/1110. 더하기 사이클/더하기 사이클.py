n = int(input())
num = n
count = 0
#10
while True:
    a = num // 10 # 1
    b = num % 10 # 0
    c = (a + b)%10 # 1
    
    num = b*10 + c #1

    count+=1
    
    if n == num:
        break
        
print(count)

