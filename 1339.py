N=int(input())

# 입력할 단어 변수 선언
words = []

# 입력받기
for _ in range(N):
    words.append(input())

# 딕셔너리 초기화
dict = {}

# 딕셔너리에 알파벳별로 값을 집어 넣어준다.
for word in words:
  # 길이를 계산하여 10^square_root만큼 넣어주기 위해
  # -1를 하는 이유는 맨뒤는 1의자리이기 때문에
  # 0 제곱을 해야 한다.
    square_root = len(word) - 1
    for c in word:
        if c in dict: # 값이 있는경우 더해준다.
            dict[c] += pow(10, square_root)
        else: # 없는경우 그대로 넣어준다.
            dict[c] = pow(10, square_root)
        # 제곱근을 뺴준다.
        square_root -= 1 

# 딕셔너리를 큰값부터 쓰기 위해 정렬
dict = sorted(dict.values(), reverse=True)

# 값 계산할 변수 선언
result,m = 0,9

# 값 계산하기
for value in dict:
    result += value * m
    print('')
    m -= 1

print(result)

"""
출처
https://jokerldg.github.io/algorithm/2021/03/13/word-math.html

이 문제의 Key Point:
- 자릿수와 알파벳을 매칭하기 위해서 Dict를 사용한 것
- pow(10, square_root)를 사용해서 자릿수를 배분한 것 (ABC라면 A가 100의 자리니까 {A:100})
    다만 맨 뒤는 1의 자리이기 때문에 square_root를 len(word)-1부터 시작
- dict로 분류했지만 reverse로 sorting하고 나면 key는 필요없으므로 list 형태로 사용 (sorted(dict.values(),reverse=True))
- 알파벳이 중복되어서 나오더라도, 그 값을 따로 생각할 필요 없이 그 값을 더 해주면 됨 (100*9+10*9이랑 110*9는 똑같음)
"""