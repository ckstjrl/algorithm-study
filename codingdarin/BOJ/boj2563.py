# BOJ 2563. 색종이 (D1 / S5)
# https://www.acmicpc.net/problem/2563


# 100x100 도화지
paper = [[0] * 100 for _ in range(100)]

# 색종이 개수
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    
    # 색종이 붙이기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
# 색종이 붙은 칸 세기
ans = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            ans += 1
            
print(ans)