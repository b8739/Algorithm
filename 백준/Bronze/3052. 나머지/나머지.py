arr = []

for n in range(10):
    val = int(input())
    arr.append(val%42)

result = set(arr)
print(len(result))