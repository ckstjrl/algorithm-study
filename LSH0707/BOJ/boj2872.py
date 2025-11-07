import sys
input = sys.stdin.readline
N = int(input())
arr = [0] * N
for i in range(N):
    x = int(input())
    arr[i] = x
arr = arr[::-1]  # (위,...,아래) -> (아래 -> 위)
start = N  # 아래에 위치시켜야 할 책 번호
cnt = 0  # 옮긴 횟수
for x in arr:
    if x == start:  # 아래에 위치시킬 책인 경우 다음으로 큰번호의 책 기록
        start = start - 1
    else:  # 다른 책인 경우 옮긴 횟수+1
        cnt = cnt + 1
print(cnt)