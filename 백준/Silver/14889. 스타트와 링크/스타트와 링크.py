from itertools import combinations
import math 
import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int,input().split())) for i in range(n)]

teams = list(combinations(range(1,n+1),n//2))
# print(teams)

difference = math.inf

for i in range(len(teams)//2):
    # print(teams[i])
    start_team = 0
    link_team = 0

    start_couples = list(combinations(teams[i],2))
    link_couples = list(combinations(teams[-1-i],2))

    #스타트팀 시너지 더하기
    for j in range(len(start_couples)):
        start_team += s[start_couples[j][0]-1][start_couples[j][1]-1] 
        start_team += s[start_couples[j][1]-1][start_couples[j][0]-1] 

    
    #링크팀 시너지 더하기
    for j in range(len(link_couples)):

        link_team += s[link_couples[j][0]-1][link_couples[j][1]-1] 
        link_team += s[link_couples[j][1]-1][link_couples[j][0]-1] 
    
    difference = min(difference,abs(start_team-link_team))

print(difference)