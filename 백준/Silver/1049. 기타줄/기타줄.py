N,M = map(int,input().split())

package = []
single = [] 

for i in range(M):
    a,b = map(int,input().split())
    package.append(a)
    single.append(b)

package_min = min(package)
single_min = min(single)

#single의 단가가 더 비쌀 때
if package_min < single_min*6:
    # 6으로 나누어 떨어지지 ㅇ낳는 나머지 값을 계산하려 할 때, 패키지 값보다 낱개 값이 더 비싸면 "패키지 값 선택" 
    if package_min < (N%6)*single_min:
        print((N//6)*package_min+package_min)
    else: 
        print((N//6)*package_min+(N%6)*single_min)

#package의 단가가 더 비쌀 때
elif package_min >= single_min:
    print(N*single_min)



