import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))
sum = 0

for i in score:
    sum += i / max(score) * 100

print(sum/N)