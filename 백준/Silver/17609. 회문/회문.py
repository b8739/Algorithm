T = int(input())

def isPseudo(word,left,right):
    while right>left:
        if word[left] == word[right]:
            left+=1
            right-=1
        else: 
            return False
    return True

def isPalindrome(word,left,right):
    if word==word[::-1]:
        return 0
    else:
        while left<right:
            if word[left]!=word[right]:
                if isPseudo(word,left+1,right) or isPseudo(word,left,right-1):
                    return 1
                else: return 2
            else:
                left+=1
                right-=1


for i in range(T):
    word = input()
    result  = isPalindrome(word,0,len(word)-1)
    print(result)

"""
left는 시작, right은 끝으로 해서, 값이 같은지 보고, 끝까지 같다면 0
만약 다르다면,
"""