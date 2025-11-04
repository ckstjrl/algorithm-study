import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

row = (H + N) // (N + 1)
col = (W + M) // (M + 1)

print(row*col)