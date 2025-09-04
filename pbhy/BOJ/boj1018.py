# 1018. 체스판 다시 칠하기
'''
8×8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

<브루트포스 알고리즘>
c1 = 'WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW','WBWBWBWB', 'BWBWBWBW'
c2 = 'BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB','BWBWBWBW', 'WBWBWBWB'
'''
N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

# 체스판 패턴 두 가지 만들기
c1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]

c2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]
a_cnt = 64  # 최대 8*8칸 다 다시 칠하는 경우

# 모든 시작 위치 (i,j)에서 8x8 체스판 자르기
for i in range(N - 7):  # N-8+1
    for j in range(M - 7):  # N-8+1
        cnt1 = 0  # c1과 다를 때 칠해야 하는 개수
        cnt2 = 0  # c2와 다를 때 칠해야 하는 개수
        for x in range(8):
            for y in range(8):
                if arr[i+x][j+y] != c1[x][y]:
                    cnt1 += 1
                if arr[i+x][j+y] != c2[x][y]:
                    cnt2 += 1
        if cnt1 < a_cnt:
            a_cnt = cnt1
        if cnt2 < a_cnt:
            a_cnt = cnt2
print(a_cnt)
