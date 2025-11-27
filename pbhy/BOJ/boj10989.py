# 10989. 수 정렬하기 3

import sys

input = sys.stdin.readline

N = int(input())
count = [0] * 10001    # 10001 크기의 리스트 정의

# N개의 정수를 리스트의 인덱스로 접근하여 개수 세기
for _ in range(N):
    num = int(input())
    count[num] += 1

# 리스트에 접근해 그 개수만큼 인덱스 출력
for i in range(10001):
    # count[i]이 1 이상이라면
    if count[i] != 0:
        # 그 값만큼 출력
        for j in range(count[i]):
            print(i)