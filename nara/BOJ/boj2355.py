import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A > B:
    start = B
    end = A
else:
    start = A
    end = B

print(end * (end + 1) // 2 - (start-1) * start // 2)