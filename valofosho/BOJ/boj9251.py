A = input()
B = input()
M = len(A)
N = len(B)
# 테이블에서 0으로 감싸는 패딩 부분을 위해서 M+1, N+1로 테이블 선언
table = [[0] * (M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        # 단어 내 글자가 동일한 위치라면 
        if A[j-1] == B[i-1]:
            # 이전 대각의 값에 + 1
            table[i][j] = table[i-1][j-1] + 1
        # 다른 값이라면 이전까지 글자(A[:i-1], B[:j] & A[:i], B[:j-1] 까지 겹치는 값 중 큰 값 선택)
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
print(table[N][M])
