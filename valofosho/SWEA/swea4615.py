"""
재미있는 오셀로 게임
기준 열, 행 으로 입력 들어온다
시작점은 0,0 이 아닌 1,1 
놓을 수 없는 지점에 놓지 않는다
연속해서 가다가 돌 안바뀌면 그냥 냅둔다
흑돌은 1, 백돌 2
2 1
1 2
위 형식으로 선착수

필요 정의 함수
1. check() -> maps내 범위 체크 
2. move() -> 돌 놓고 돌 뒤집기
3. 메인
"""
def check(i,j,N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def move(r, c, color, N):
    dr = [1, 1, 1, -1, -1, -1, 0, 0]
    dc = [0, -1, 1, 0, -1, 1, 1, -1]
    # 문제의 1-based index를 0-based index로 변경
    r, c = r-1, c-1
    maps[r][c] = color
    for d in range(8):
        arr = [] # 변경할 돌의 좌표를 담는 리스트 선언
        for k in range(1,N+1):
            nr, nc= r+dr[d]*k, c+dc[d]*k    # 8방향을 순회하며 연결된 돌을 찾는다
            if check(nr, nc, N) and maps[nr][nc] == color:  # 범위 내에 있으며, 착수와 동일한 돌인 경우
                if not arr: # 처음으로 만난 경우 바로 돌아감
                    break
                else:
                    for i, j in arr: # 돌들을 만나고 같은 색을 만나면 이전의 돌들을 색 변경
                        maps[i][j] = color
                    break   # 돌들을 모두 바꿔주고 바로 탈출
            elif check(nr,nc,N) and maps[nr][nc] == 0:  # 범위내에 있지만 빈 칸을 만나면 탈출
                break
            elif check(nr,nc,N) and maps[nr][nc] != color:  # 범위 내에서 다른 색의 돌을 만난 경우 좌표 담기
                arr.append([nr,nc])
            else:
                break
    return


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N * N maps 정의
    maps = [[0] * N for _ in range(N)]
    # 초기 값 착수
    maps[N//2-1][N//2-1], maps[N//2][N//2] = 2, 2
    maps[N//2-1][N//2], maps[N//2][N//2-1] = 1, 1
    # 움직일 수 있는 8방향 설정
    for _ in range(M):
        c, r, color = map(int, input().split())
        move(r, c, color, N)

    cnt_1 = 0
    cnt_2 = 0
    for row in maps:
        cnt_1 += row.count(1)
        cnt_2 += row.count(2)
    print(f"#{test_case} {cnt_1} {cnt_2}")