num = int(input())
for n in range(num):
    result = ''
    p,word = input().split()
    for w in word:
        result += w*int(p)
    print (result)    
        