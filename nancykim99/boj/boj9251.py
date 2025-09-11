# BOJ9251. LCS
# lcs[i][j]를 구할 때, 2개의 문자열을 비교
# 비교한 문자가 같지 않다면, [i-1][j]과 [i][j-1] 중에 더 큰 값
# 비교한 문자가 같다면, [i-1][j-1] + 1 값

# 2차원 memoization 만들기
A = list(input())
B = list(input())
N = len(A) + 1
M = len(B) + 1

lcs = [[0] * M for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if A[i-1] == B[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

# 2차원에서 max구하기
print(max(map(max, lcs)))