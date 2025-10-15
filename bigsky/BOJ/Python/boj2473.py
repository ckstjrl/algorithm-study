# BOJ2473(D3): 세 용액
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

best = float('inf')

for i in range(N - 2):
    l, r = i + 1, N - 1
    while l < r:
        s = A[i] + A[l] + A[r]
        if abs(s) < best:
            best = abs(s)
            ans = (A[i], A[l], A[r])
            if best == 0:
                print(*ans)
                sys.exit(0)
        if s > 0:
            r -= 1
        else:
            l += 1
            
print(*ans)