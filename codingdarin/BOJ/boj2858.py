# BOJ 2858. 기숙사 바닥 (D1 / B2)
# https://www.acmicpc.net/problem/2858

r, b = map(int, input().split())

total = r + b  # 전체 타일 개수

# 가능한 모든 가로 길이 시도
for W in range(3, total+1):
    if total % W == 0:  # W가 약수인 경우
        L = total // W  # 세로 길이 계산
        if (W-2) * (L-2) == b:  # 내부 영역이 갈색 타일 개수와 일치하는지 확인
            print(L, W)  # L >= W (세로, 가로)
            break