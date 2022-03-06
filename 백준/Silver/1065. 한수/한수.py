num = int(input())

cnt = 0
for n in range(1,num+1): #0-999
    num_list = list(map(int, str(n)))
    if n<100:
        cnt+=1    
    elif num_list[0]-num_list[1]==num_list[1]-num_list[2]:
        cnt+=1
print(cnt)
