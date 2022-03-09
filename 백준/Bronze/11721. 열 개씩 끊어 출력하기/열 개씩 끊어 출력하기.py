s = input()

cnt = 0
w = ''

if len(s)<10:
    print(s)
else:
    for i in s:
        cnt+=1
        w+=i
        if cnt%10==0:
            print(w)
            w = ''
            
if w != '':
    print(w)