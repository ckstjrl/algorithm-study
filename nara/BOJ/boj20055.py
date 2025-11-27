import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
q = deque(map(int, input().split()))

robot = deque([False] * 2 * N)
cnt = 0 # 내구도 0인 칸의 개수
result = 0 # 몇 번째 단계

while cnt < K:
    # 벨트 회전
    # q.rotate(N) : 오른쪽으로 N칸 회전
    q.rotate(1)
    robot.rotate(1)

    # 로봇 내림
    if robot[N-1]:
        robot[N-1] = False

    # 로봇 이동
    # 가장 먼저 올라간 로봇부터, 이동가능하면 이동(앞 칸 내구도 0이면 가만히)
    for i in range(2*N-1, -1, -1):
        if robot[i] and not robot[i+1] and q[i+1] >= 1:
            robot[i] = False
            robot[i+1] = True
            q[i+1] -= 1

    # 로봇 올림
    if q[0] != 0:
        q[0] -= 1
        robot[0] = True

    # 로봇 내림
    if robot[N-1]:
        robot[N-1] = False

    result += 1
    cnt = q.count(0)
print(result)
