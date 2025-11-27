# 2005. 파스칼의 삼각형 / D2

T = int(input())
for t in range(T):
    N = int(input())
    pascal = [[1]*(i+1) for i in range(N)]  # 기본적으로 삼각형을 1로 채우기

    for i in range(2, N):
        for j in range(1, i):  # 양 끝이 아닌 부분들만
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]  # 자신의 왼쪽 위 + 오른쪽 위

    print(f'#{t+1}')
    for p in pascal:
        print(*p)