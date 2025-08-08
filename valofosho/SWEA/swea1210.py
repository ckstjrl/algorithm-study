# arr의 범위를 벗어나는지 확인하는 함수
def check(i, j):
    if 0<=i<100 and 0<=j<100:
        return True
    else:
        return False


for test_case in range(1,11):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 끝 행에서 2인 값의 위치 반환
    si = 99
    sj = arr[si].index(2)
    # 시작 인덱스 = arr[99][sj]
    # 이동 방향은 상, 좌, 우 3가지로 제한
    # 만약에 3 방향을 모두 이동 가능하면 좌 or 우(양방향) -> 상
    di = [0, 0, -1]
    dj = [1, -1, 0]
    d = 0
    # 아래에서 위로 끝점(arr[0][x])을 향해 순회한다
    while si != 0:
        ni,nj = si+di[d], sj+dj[d]
        if check(ni,nj) and arr[ni][nj] == 1:
            arr[ni][nj] = 0
            si,sj = ni, nj
            # 사다리에서 아래에서 위로 내려갈 때 꺾이는 것을 우선
            d = 0
        else:
            d = (d+1) % 3
    print(f"#{test_case} {sj}")
