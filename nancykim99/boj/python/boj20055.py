'''
BOJ20055 : 컨베이어 벨트 위의 로봇 (S5)

해결 방법 : 
1. 라운드 한 번 돌때마다 0인 칸 세기
2. 벨트 돌리기
3. 벨트 돌릴때마다 로봇 밀거나 제거하기 : 인덱싱으로

메모 : 
queue에 rotate()를 사용한 정답 코드들이 찾아보니 많았다.
나중에 사용해보면 좋을듯
일단 벨트를 수동으로 하나씩 움직였는데, 여기서 시간을 줄일 수 있는 방법을 찾고 싶다
`def rotate_belt(conveyor):
    turnover = n                          # 윗줄 길이 = n
    conveyor_up = conveyor[:turnover]     # 0 ~ n-1 (윗줄)
    conveyor_down = conveyor[turnover:]   # n ~ 2n-1 (아랫줄)
    going_up = conveyor_down.pop()        # 아랫줄 마지막 → 윗줄 앞으로
    conveyor_up.insert(0, going_up)
    going_down = conveyor_up.pop()        # 윗줄 마지막 → 아랫줄 앞으로
    conveyor_down.insert(0, going_down)
    return conveyor_up + conveyor_down`
'''

n, k = map(int, input().split())
belt = list(map(int, input().split()))   # 2n개
robot = [0] * n                          # 윗줄 n칸에 대한 로봇 위치만 관리

# 0인 칸 세기
def cnt_blank(conveyor):
    cnt = 0
    for x in conveyor:
        if x == 0:
            cnt += 1
    return cnt

# 벨트 돌리기
def rotate_belt(conveyor):
    turnover = n                          # 윗줄 길이 = n
    conveyor_up = conveyor[:turnover]     # 0 ~ n-1 (윗줄)
    conveyor_down = conveyor[turnover:]   # n ~ 2n-1 (아랫줄)
    going_up = conveyor_down.pop()        # 아랫줄 마지막 → 윗줄 앞으로
    conveyor_up.insert(0, going_up)
    going_down = conveyor_up.pop()        # 윗줄 마지막 → 아랫줄 앞으로
    conveyor_down.insert(0, going_down)
    return conveyor_up + conveyor_down

cnt_round = 0
while True:
    cnt_round += 1

    # 벨트 + 로봇 회전하기
    belt = rotate_belt(belt)
    robot = [0] + robot[:-1]             # 오른쪽으로 한 칸 밀기
    robot[-1] = 0                        # 내리는 위치(n-1)에서 로봇 제거

    # 로봇 이동 (뒤에서 앞으로, 겹치지 않게)
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    robot[-1] = 0                        # 다시 한 번 내리는 위치 비우기

    # 0번 칸에 로봇 올리기
    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

    # 내구도 0인 칸 개수 확인
    if cnt_blank(belt) >= k:
        break

print(cnt_round)






