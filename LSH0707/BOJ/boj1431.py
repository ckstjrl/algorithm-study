import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    a = input().strip()
    x = len(a)  # 문자열 길이
    y = 0  # 문자열 내 숫자 합
    for i in a:
        if i.isdecimal():
            y = y + int(i)
    arr.append((x, y, a))
arr.sort()  # 정렬 (길이 -> 숫자 합 -> 사전순)
for i in range(N):
    print(arr[i][2])
