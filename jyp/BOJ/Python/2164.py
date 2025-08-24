from collections import deque
N = int(input())

cards = deque(i for i in range(1,N+1))
while len(cards) > 1:
    cards.popleft()
    if len(cards) > 1:
        bottom = cards.popleft()
        cards.append(bottom)

print(cards[0])
    

