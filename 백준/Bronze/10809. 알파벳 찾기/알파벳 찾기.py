word = input()
alphabet = list(range(97,123))  # 아스키코드 숫자 범위

for a in alphabet:
    ans = word.find(chr(a))
    print(f'{ans}',end=' ')