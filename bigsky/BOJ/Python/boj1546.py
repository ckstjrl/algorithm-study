# BOJ1546(D1): 평균
from statistics import mean
import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

ans = mean(scores) / max(scores) * 100
print(ans)