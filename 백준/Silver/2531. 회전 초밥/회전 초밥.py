import sys
from collections import defaultdict

N,D,K,C = map(int,input().split())

# input = sys.stdin.readline
#초밥 배열
S = []

#초밥 종류 딕셔너리
sushiType= defaultdict(int)

#초밥번호 받기
for i in range(N):
    sushi = int(input())
    S.append(sushi)
    # sushiType[sushi] = 0

#슬라이딩 윈도우
S.extend(S) 

# 시작 전에 일단 K만큼 더해주기
for i in range(K):
    sushiType[S[i]]+=1

maxv = len(sushiType)

for i in range(K,len(S)):
    sushiType[S[i-K]]-=1
    if sushiType[S[i-K]]==0:
        del sushiType[S[i-K]]
    sushiType[S[i]]+=1
    # 보너스
    sushiType[C] = 1
              
    maxv = max(maxv,len(sushiType))

print(maxv)

