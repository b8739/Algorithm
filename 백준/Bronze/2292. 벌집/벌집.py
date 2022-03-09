start = 1

destination = int(input()) #36
cnt = 1

while start < destination:
    start += 6*cnt
    cnt += 1    
print(cnt)
