n = int(input())
count = [0] * n


for idx in range(n):
    cons = 0
    count[idx] = 0
    quiz_result = input()
    
    for result in quiz_result:
        if result == 'O':
            count[idx] += cons+1
            cons += 1
        else:
            cons = 0
            continue
            
for value in count:
    print(value)