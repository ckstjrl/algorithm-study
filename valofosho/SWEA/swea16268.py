# 배열 내에서 움직이는지 확인하는 함수
def check(i,j,N,M):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False
    
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N행 M열
    cnt = 0
    # 방향은 하, 상, 우, 좌
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            # 초기 중앙 값 설정
            cen = arr[i][j]
            # 4 방향을 모두 순회
            for d in range(4):
                # 갈 수 있는 길이라면 풍선을 터트리고 값에 추가
                if check(i+di[d],j+dj[d], N, M):
                    cen += arr[i+di[d]][j+dj[d]]
            if cnt < cen:
                cnt = cen
    print(f"#{test_case} {cnt}")