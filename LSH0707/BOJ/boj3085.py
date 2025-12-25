import sys
input = sys.stdin.readline
N = int(input())
arr = [list(input().strip()) for _ in range(N)]
def cnt():
    max_cnt = 0
    for p in range(N):
        cnt_i = 0
        cnt_j = 0
        b_i = ''
        b_j = ''
        for q in range(N):
            if q == 0:
                b_i = arr[p][0]  # 직전 문자 기록
                b_j = arr[0][p]  # 직전 문자 기록
                cnt_i = 1  # 같은 문자 횟수 기록(가로)
                cnt_j = 1  # 같은 문자 횟수 기록(세로)
            else:
                if arr[p][q] == b_i:  # 가로-같은 문자면 cnt+1, 다르면 최대길이 기록하고 1로초기화
                    cnt_i = cnt_i + 1
                if arr[p][q] != b_i:
                    if cnt_i > max_cnt:
                        max_cnt = cnt_i
                    cnt_i = 1
                    b_i = arr[p][q]
                if arr[q][p] == b_j:  # 세로
                    cnt_j = cnt_j + 1
                if arr[q][p] != b_j:
                    if cnt_j > max_cnt:
                        max_cnt = cnt_j
                    cnt_j = 1
                    b_j = arr[q][p]
        max_cnt = max(cnt_i, cnt_j, max_cnt)
    return max_cnt
max_c = 0
for a in range(N):
    for b in range(N-1):
        if arr[a][b] != arr[a][b+1]:  # 왼쪽 오른쪽 비교하고 다르면 바꾸고 함수
            arr[a][b], arr[a][b+1] = arr[a][b+1], arr[a][b]
            tmp = cnt()
            if tmp > max_c:
                max_c = tmp
            arr[a][b], arr[a][b+1] = arr[a][b+1], arr[a][b]
        if arr[b][a] != arr[b+1][a]:  # 위 아래 비교하고 다르면 바꾸고 함수
            arr[b][a], arr[b+1][a] = arr[b+1][a], arr[b][a]
            tmp = cnt()
            if tmp > max_c:
                max_c = tmp
            arr[b][a], arr[b+1][a] = arr[b+1][a], arr[b][a]
print(max_c)