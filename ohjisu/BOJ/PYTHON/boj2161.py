from collections import deque

N = int(input())

cards = deque(range(1, N+1))
throw = deque()

while cards :
    throw.append(cards.popleft())
    if cards :
        cards.append(cards.popleft())

print(*throw)