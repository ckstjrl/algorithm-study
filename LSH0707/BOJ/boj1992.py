import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]
def check(si, sj, N):  # (시작좌표, 배열 크기)
    x = arr[si][sj]  # 시작좌표 값
    for i in range(si, si + N):  # 정사각형
        for j in range(sj, sj + N):
            if arr[i][j] != x:  # 하나라도 시작좌표값이랑 다르면 False 리턴
                return False
    return True  # 같으면 True 리턴
ans = ''
def quad(si, sj, N):
    global ans
    if check(si, sj, N):  # 모두 같은 값이면 ans에 기록하고 리턴
        ans = ans + str(arr[si][sj])
        return
    ans = ans + '('  # 시작 괄호
    quad(si, sj, N//2)  # 왼위 오위 왼아 오아 재귀
    quad(si, sj + N//2, N//2)
    quad(si + N//2, sj, N//2)
    quad(si + N//2, sj + N//2, N//2)
    ans = ans + ')'  # 끝 괄호
quad(0, 0, N)
print(ans)