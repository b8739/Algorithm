from collections import deque

N = int(input())

card = deque([i for i in range(1,N+1)])

while len(card)!=1:
    card.popleft()
    to_first = card.popleft()
    card.append(to_first)
print(card.popleft())

            

