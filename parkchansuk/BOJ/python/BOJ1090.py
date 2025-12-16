# BOJ 1090. 체커 / D3
'''
문제
N개의 체커가 엄청 큰 보드 위에 있다. i번 체커는 (xi, yi)에 있다. 같은 칸에 여러 체커가 있을 수도 있다.
체커를 한 번 움직이는 것은 그 체커를 위, 왼쪽, 오른쪽, 아래 중의 한 방향으로 한 칸 움직이는 것이다.

입력
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에 각 체커의 x좌표와 y좌표가 주어진다. 이 값은 1,000,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 수 N개를 출력한다. k번째 수는 적어도 k개의 체커가 같은 칸에 모이도록 체커를 이동해야 하는 최소 횟수이다.
'''
import sys
input = sys.stdin.readline

N = int(input())
checker_axis = []
for _ in range(N):
    x, y = map(int, input().split())
    checker_axis.append((x, y))

# 체커는 체커가 존재하는 좌표들 범위 내부에서만 움직이게 된다.
xs = sorted({x for x, _ in checker_axis}) # 체커들의 x좌표를 set 형태로 모아서 중복을 제거하고 sort한 list로 저장
ys = sorted({y for _, y in checker_axis}) # 체커들의 y좌표를 set 형태로 모아서 중복을 제거하고 sort한 list로 저장

INF = 10**30 # 최솟값을 구해야 하므로 최대한 큰 값 설정
min_move = [INF]*N

# 체커가 움직일 가능성 있는 좌표까지 각 체커들이 갈때 필요한 움직임을 리스트로 저장
# min_move[0]는 1개, min_move[1]는 2개, ... min_move[n-1]는 N개가 해당 좌표로 왔을때 움직임의 최솟값
# 가능성 있는 좌표들을 돌면서 최솟값 갱신
for ex in xs:
    for ey in ys:
        arr = [abs(checker_axis[i][0]-ex) + abs(checker_axis[i][1] - ey) for i in range(N)]
        arr.sort()
        print(arr)
        s = 0
        for k in range(N):
            s += arr[k]
            if s < min_move[k]:
                min_move[k] = s

print(*min_move)


# 체커가 체커가 존재하는 좌표로만 움직인다 생각함...
'''
N = int(input())
checker_axis = []
for _ in range(N):
    x, y = map(int, input().split())
    checker_axis.append((x, y))

move = [[0]*N for _ in range(N)]
for i in range(N):
    fx, fy = checker_axis[i][0], checker_axis[i][1]
    for j in range(N):
        sx, sy = checker_axis[j][0], checker_axis[j][1]
        dx = abs(sx - fx)
        dy = abs(sy - fy)
        move[i][j] = dx+dy

move_sum = [[0]*N for _ in range(N)]
for a in range(N):
    arr = sorted(move[a])
    move_sum[0][a] = arr[0]
    for b in range(1, N):
        move_sum[b][a] = move_sum[b-1][a] + arr[b]

for j in range(N):
    print(min(move_sum[j]), end=' ')
'''

# 메모리 초과
'''
N = int(input())
checker_axis = []
for _ in range(N):
    x, y = map(int, input().split())
    checker_axis.append((x, y))

# 체커는 체커들 좌표 범위 내부에서만 움직인다.
checker_axis.sort(key=lambda x:x[0]) 
x_min = checker_axis[0][0]
x_max = checker_axis[N-1][0]
checker_axis.sort(key=lambda x:x[1])
y_min = checker_axis[0][1]
y_max = checker_axis[N-1][1]

# 체커가 움직일 수 있는 좌표를 리스트화 진행
axis = [(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)]

# 각 좌표들에 채커가 이동할 떄까지의 움직일을 구해서 이차원 배열로 작성
axis_move = [[0]*N for _ in range(len(axis))]
for i in range(len(axis)):
    ex, ey = axis[i]
    for j in range(N):
        sx, sy = checker_axis[j]
        dx = abs(sx - ex)
        dy = abs(sy - ey)
        axis_move[i][j] = dx + dy

# 해당 좌표까지 온 움직임을 sort해서 작은 숫자부터 더해가며 N개가 이동했을 때의 움직임을 저장함
# 1개의 체커가 움직인 경우 0행, 2개의 채커가 움직인 경우 1행 ... N개의 채커가 움직인 경우 N-1행에 저장
# 해당 행마다 min을 뽑아내면 답

move_sum = [[0]*len(axis) for _ in range(N)]
for a in range(len(axis)):
    arr = sorted(axis_move[a])
    move_sum[0][a] = arr[0]
    for b in range(1, N):
        move_sum[b][a] = move_sum[b - 1][a] + arr[b]

for j in range(N):
    print(min(move_sum[j]), end=' ')
'''

# 메모리 초과 2
'''
axis = [(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)] # 체커들이 움직일 수 있는 좌표

INF = 1e10
min_move = [INF]*N

# 위와 동일한 방식이지만, axis_move와 move_sum을 만드는 것이 메모리 초과의 원인이라 행마다 최솟값을 저장하고 지우는 걸로 코드 구성
for ex, ey in axis:
    arr = [abs(sx - ex) + abs(sy - ey) for sx, sy in checker_axis]
    arr.sort()

    s = 0
    for k in range(N):
        s += arr[k]
        if s < min_move[k]:
            min_move[k] = s

print(*min_move)
'''

# 시간 초과
'''
N = int(input())
checker_axis = []
for _ in range(N):
    x, y = map(int, input().split())
    checker_axis.append((x, y))

checker_axis.sort(key=lambda x:x[0])
x_min = checker_axis[0][0]
x_max = checker_axis[N-1][0]
checker_axis.sort(key=lambda x:x[1])
y_min = checker_axis[0][1]
y_max = checker_axis[N-1][1]

INF = 1e10
min_move = [INF]*N

# axis를 만드는 것도 메모리 초과의 원인이라 생각해서 코드 변경
# But, 이렇게 하면 극단적으로 차이가 심한 점이 있는 경우 그 사이 좌표까지 모두 연산해야해서 시간 초과 발생
for ex in range(x_min, x_max+1):
    for ey in range(y_min, y_max):
        arr = [abs(sx - ex) + abs(sy - ey) for sx, sy in checker_axis]
        arr.sort()

        s = 0
        for k in range(N):
            s += arr[k]
            if s < min_move[k]:
                min_move[k] = s

print(*min_move)
'''

'''
문제 잘못이해 1번
메모리 초과 2번
시간초과 1번
이 과정을 통해 코드 점점 업그레이드
일단 체커는 무조건 체커들 좌표 범위 내부에서만 움직일 수 밖에 없음
하지만 모든 좌표를 검수하는 것은 시간 초과를 발생하게 하므로
체커가 가지고 있는 x, y좌표만 중복을 제거하여 리스트화 시킴
체커가 움직일 가능성 있는 좌표까지 각 체커들이 갈때 필요한 움직임을 리스트로 저장
min_move[0]는 1개, min_move[1]는 2개, ... min_move[n-1]는 N개가 해당 좌표로 왔을때 움직임의 최솟값
가능성 있는 좌표들을 돌면서 최솟값 갱신
min_move를 출력
'''