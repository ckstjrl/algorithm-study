# BOJ 2164. 카드2 / D2
import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([i for i in range(1, N+1)])

while len(card) > 1:
    card.popleft()
    card.rotate(-1)

print(card[0])