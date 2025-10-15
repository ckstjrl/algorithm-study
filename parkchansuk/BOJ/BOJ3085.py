# BOJ 3085. 사탕 게임 / D2
'''
문제
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다.
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

출력
첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.
'''
import sys
input = sys.stdin.readline

def check(arr):
    best = 1
    # 가로
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                best = max(best, cnt)
                cnt = 1
        best = max(best, cnt)

    # 세로
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if arr[i][j] == arr[i-1][j]:
                cnt += 1
            else:
                best = max(best, cnt)
                cnt = 1
        best = max(best, cnt)

    return best

N = int(input().strip())
arr = [list(input().strip()) for _ in range(N)]

ans = check(arr) # 기본상태 확인
for i in range(N):
    for j in range(N):
        # 오른쪽과 교환
        if j + 1 < N and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            ans = max(ans, check(arr))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 원상복구

        # 아래쪽과 교환
        if i + 1 < N and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            ans = max(ans, check(arr))
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] # 원상복구

print(ans)

'''
가로 세로에서 같은 색이 몇개 나오는지 확인하고 최댓값을 뽑아내는 함수를 작성
이후 가로축으로 다를때 교환하고 확인하고 원상복구 반복
이후 세로축도 동일하게 진행
제일 큰 값이 ans로 출력
'''