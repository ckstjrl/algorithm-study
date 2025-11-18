# 20055. 컨베이어 벨트 위의 로봇

from collections import deque
N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))   # 벨트 위치별 내구도 저장
step_cnt = 1    # 수행중인 단계 수 
robot_present = deque([False] * N)  # 해당 위치에 로봇이 있는지를 T/F로 저장
start = 0       # 올리는 위치 (0 고정)
end = N - 1     # 내리는 위치 (N-1 고정)

while True:
    ## 1. 벨트 회전, 로봇 회전 (내구도 소모 X)
    belt.appendleft(belt.pop())     # 벨트 회전
    robot_present.appendleft(robot_present.pop())   # 로봇 위치도 같이 회전
    robot_present[end] = False  # 내리는 위치에 로봇 있으면 바로 내림

    ## 2. 로봇 이동 (내구도 소모 O)
    for i in range(N-2, -1, -1):    # 내리는 위치와 가까운 위치부터 탐색
        # i위치에 로봇이 있고, 이동할 위치에는 로봇이 없고, 이동할 칸의 내구도가 1 이상
        if robot_present[i] and not robot_present[i+1] and belt[i+1] > 0:
            # 로봇 위치 i -> i+1로 이동
            robot_present[i] = False
            robot_present[i+1] = True
            belt[i+1] -= 1      # 내구도 소모
    robot_present[end] = False  # 내리는 위치에 로봇 있으면 바로 내림
    
    ## 3. 로봇 올리기
    # 올리는 위치의 내구도 1 이상이고, 올리는 위치에 로봇 없으면
    if belt[start] > 0 and not robot_present[start]:
        robot_present[start] = True     # 올리는 위치에 로봇 올림
        belt[start] -= 1    # 내구도 소모

    if belt.count(0) >= K:  # 내구도 0인 칸 개수가 K개 이상이면 종료
        break
    step_cnt += 1   # 단계 +1

    # --- 실패한 코드: 인덱스 조절해서 벨트 회전시키기  ---
    # # 1. 벨트 회전
    # start = start - 1 if start > 0 else 2*N - 1
    # end = end - 1 if end > 0 else 2*N - 1
    #
    # # 2. 로봇 이동
    # new_robot = []
    # for r in robot:
    #     nxt = r+1 if r < 2*N-1 else 0
    #     if belt[nxt] > 0 and nxt not in new_robot:
    #         belt[nxt] -= 1
    #         if nxt != end:
    #             new_robot.append(nxt)
    # robot = new_robot
    #
    # # 3. 로봇 올리기
    # if belt[start] > 0 and start not in robot:
    #     robot.append(start)
    #     belt[start] -= 1

print(step_cnt)