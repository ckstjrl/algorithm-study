import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    tmp = list(map(int, input().split()))

    print(min(tmp))