"""
BOJ 14719 - 빗물

문제 정의
1. 세로 H, 가로 W가 주어진다
2. 0 이상 H 이하의 정수가 건물 높이로 주어짐
3. 블록 사이에 빗물이 1씩 쌓인다면 고이는 빗물의 총량은?

로직 정의
1. 순회해야하는 조건인 W가 500으로 작은 편
2. 가로를 전체 순회하면서 좌측, 우측에서 가장 큰 값을 찾는다.
3. 가장 큰 두 값중 작은 것을 택해 현재 값과의 높이 차가 빗물이 쌓인 것
"""
import sys
input = sys.stdin.readline

W, H = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in range(1,H-1):
    left, right = 0, 0
    for l in range(0,i):
        left = max(arr[l], left)
    for r in range(i+1, H):
        right = max(arr[r], right)
    temp = max(0, min(left, right) - arr[i])
    ans.append(temp)
print(sum(ans))
