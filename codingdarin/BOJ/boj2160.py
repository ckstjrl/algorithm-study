# BOJ2160. 그림 비교 (D1 / B1)


n = int(input())
arr = [[] for _ in range(n+1)] # 0자리 패딩한 빈 배열들

# 각 그림을 자리 맞춰 배열에 넣기
for i in range(1, n+1):
    for _ in range(5):
        arr[i].append(input())

# 함수 만들자
def count_diff(a, b):
    cnt = 0
    for i in range(5):
        for j in range(7):
            if arr[a][i][j] != arr[b][i][j]:
                cnt += 1
    return cnt 

min_diff = float('inf')
a = b = ''

# 완탐 시작
for i in range(1, n):
    for j in range(i+1, n+1):
        if count_diff(i,j) <= min_diff:
            min_diff = count_diff(i,j)
            a, b = i, j
            
            # 가지치기 : 최소 차이가 0이면 더 이상 볼 필요 없음
            if min_diff == 0:
                break
print(a, b)