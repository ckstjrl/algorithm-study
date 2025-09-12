# BOJ2161: 카드1
from collections import deque

N = int(input())
cards = deque(range(1, N+1))
result_order = [0] * N

for i in range(N):
    result_order[i] = cards.popleft()
    if cards:
        cards.append(cards.popleft())

print(*result_order)