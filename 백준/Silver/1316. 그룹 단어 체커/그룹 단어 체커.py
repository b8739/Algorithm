num =  int(input()) #3
cnt = 0
for n in range(num): 
    word = input() #happy
    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:
            rest = word[idx+1:]
            if rest.count(word[idx])>0: #not group
                cnt-=1
                break
            continue
    cnt += 1
print(cnt)