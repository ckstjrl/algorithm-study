# BOJ 10798. 세로읽기 (D1 / B1)
# https://www.acmicpc.net/problem/10798

import sys
input = lambda: sys.stdin.readline().rstrip()

# 각 열을 담을 리스트 배열 초기화
arr = [[] for _ in range(15)]

for _ in range(5):
    # 한 줄씩 입력 받기
    line = input()
    idx = 0
    for each in line:
        arr[idx].append(each)
        idx += 1

# 각 열을 순회하며 출력 (15줄이라 if문 생략)
for i in range(15):
    print(''.join(arr[i]), end='')