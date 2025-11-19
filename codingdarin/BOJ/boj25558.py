# BOJ 25558. 내비게이션 (D1 / B2)
# https://www.acmicpc.net/problem/25558

n = int(input())
arr = list(map(int, input().split()))

gi, gj = arr[2], arr[3]
min_distance = float('inf')
ans = ''

# 각 네비게이션에 대해
for i in range(n):
    each_total = 0
    ci, cj = arr[0], arr[1]
    m = int(input())
    # 해당 네비의 각 지점들
    for j in range(m):
        ni, nj = map(int, input().split())
        each_total += abs(ci - ni) + abs(cj - nj)
        ci, cj = ni, nj
    #골인 지점까지 계산
    each_total += abs(ci - gi) + abs(cj - gj)
    
    if min_distance > each_total:
        min_distance = each_total
        ans = i+1

print(ans)
