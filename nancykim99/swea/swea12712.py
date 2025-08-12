# 12712. 파리퇴치3 D2
# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개체 수를 의미한다.
# 파리 킬러 스프레이를 한 번만 뿌려 최대한 많은 파리를 잡으려고 한다. 스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다. 스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
# 다음은 M=3 세기로 스프레이를 분사한 경우 파리가 퇴치되는 칸의 예로, +또는 x 중 하나로 분사된다. 뿌려진 일부가 영역을 벗어나도 상관없다.
# 한 번에 잡을 수 있는 최대 파리수를 출력하라.
#
# [제약 사항]
# 1. N 은 5 이상 15 이하이다.
# 2. M은 2 이상 N 이하이다.
# 3. 각 영역의 파리 갯수는 30 이하 이다.
#
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 다음 N 줄에 걸쳐 N x N 배열이 주어진다.

T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 십자가 모양으로 퇴치할 때
    max_plus = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j] # 기준점
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for c in range(1, M):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        s += arr[ni][nj]
            if max_plus < s: # 최댓값 갱신
                max_plus = s

    # 대각선 모양으로 퇴치할 때
    max_digon = 0
    for i in range(N):
        for j in range(N):
            s = arr[i][j] # 기준점
            for di, dj in [[-1,1], [1,1], [1,-1], [-1,-1]]:
                for c in range(1, M):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        s += arr[ni][nj]
            if max_digon < s:
                max_digon = s

    # 두 최댓값 비교
    max_v = 0
    if max_digon > max_plus:
        max_v += max_digon
    else:
        max_v += max_plus

    print(f'#{tc}', max_v)

# 시행착오 1 : 대각선은 di, dj의 값을 [[-1,1], [1,1], [1,-1], [-1,-1]]로 하면 가능함
# 시행착오 2 : <와 >를 잘못 넣음...
