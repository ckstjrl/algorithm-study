# BOJ 7568. 덩치 (D1 / S5)
# https://www.acmicpc.net/problem/7568

import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

# 등수를 넣을 배열
rank = []

# 각각의 등수를 구해보자
for i in range(n):
    cnt = 1
    # 다른 모든 것과 비교했을 때 등수
    for j in range(n):
        if i != j:
            # 둘다 큰게 있으면 등수 밀림, 아니면 그대로
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1
    rank.append(cnt)

print(*rank)