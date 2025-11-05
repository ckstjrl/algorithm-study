"""
BOJ1780. 종이의 개수

[문제]
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다.
우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

[입력]
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다.
다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

[출력]
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def count_paper_pieces(y, x, size):
    first = paper[y][x]  # 현재 종이의 첫 번째 숫자
    same = True  # 현재 종이가 모두 같은 숫자로 되어 있으면 True, 아니라면 False

    # 모든 칸이 같은지 확인
    for i in range(y, y + size):
        for j in range(x, x + size):
            if paper[i][j] != first:  # 다른 숫자가 하나라도 있다면
                same = False
                break   # 반복문 탈출
        if not same:
            break   # 2중 반복문 탈출
    
    # 모든 칸이 같은 숫자라면 해당 숫자 종이의 카운트를 +1
    if same:
        count[first] += 1
        return
    
    # 다르다면, 9등분해서 재귀
    third = size // 3  # 현재 종이 크기를 3으로 나눈 한 변의 길이
    for dy in range(3):
        for dx in range(3):
            # (y + dy * third, x + dx * third)부터 시작하는 하위 종이로 재귀 호출
            count_paper_pieces(y + dy * third, x + dx * third, third)

# main
N = int(input())    # N: 종이의 한 변의 길이
paper = [list(map(int, input().split())) for _ in range(N)]  # paper: 종이 입력
count = {-1: 0, 0: 0, 1: 0}  # 카운트 배열을 0으로 초기화
count_paper_pieces(0, 0, N)  # 조건을 만족하는 종이의 개수를 세는 함수

# 결과 출력
print(count[-1])
print(count[0])
print(count[1])
