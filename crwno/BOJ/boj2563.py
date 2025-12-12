N = int(input())
board = [[0] * 101 for _ in range(101)]
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            if board[i][j] == 0:
                board[i][j] = 1
                ans += 1
print(ans)