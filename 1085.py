x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

#변경사항

# 왼쪽 모서리 (0,0)간의 거리는 x,y,에서 0을 빼는 거기 때문에 x-0, y-0 이렇게 할 필요 없이, 그냥 x,y 사용
# 값을 넣어두지 않고 print로 바로 값 출력