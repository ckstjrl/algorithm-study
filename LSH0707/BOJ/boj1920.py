import sys
input = sys.stdin.readline
N = int(input())
arr = set(map(int, input().split()))  # list보다 빠름
M = int(input())
a = list(map(int, input().split()))
for i in a:
    if i in arr:  # 세트에 있으면 1 없으면 0 출력
        print(1)
    else:
        print(0)