dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input().upper() #AJC
time = 0
for w in word:
    for idx,d in enumerate(dial):
        if w in d:
            num = idx+2
            time += num+1
print(time)
    