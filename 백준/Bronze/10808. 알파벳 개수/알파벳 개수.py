alphabet = [0]*26

word = input()

for i in word:
    alphabet[ord(i)-97]+=1

for i in alphabet:
    print(i, end=' ')