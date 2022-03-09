n = int(input())
words = []
alphabets = {}
for _ in range(n):
    words.append(input())
for w in words:
    square_root = len(w)-1
    for l in w:
        if l in alphabets:
            alphabets[l] += pow(10,square_root)
        else:
            alphabets[l] = pow(10,square_root)
        square_root-=1
    
alphabets_s = sorted(alphabets.values(),reverse=True)

sum = 0 
num = 9
for i in alphabets_s: #0-9
    sum += i * num
    num-=1
print(sum)