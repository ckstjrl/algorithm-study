'''boj3190 뱀

'Dummy' 라는 도스게임이 있다. 
이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다.
 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 
보드의 상하좌우 끝에 벽이 있다. 
게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 
뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''

N = int(input())    #보드의 크기
K = int(input())    #사과의 개수
pos = [list(map(int, input().split())) for _ in range(K)]   #사과의 행 열 위치 정보
#1행 1열이면 (0, 0) 임
for i in range(len(pos)):
    pos[i][0] -= 1  # 행 -1
    pos[i][1] -= 1  # 열 -1

L = int(input())    #뱀의 방향 변환 횟수
dir = [list(map(str, input().split())) for _ in range(L)]   
#뱀의 방향 변환 정보, X C로 이루어짐 X초가 끝난 뒤 'L'왼쪽 또는 'D'오른쪽 90도 방향 회전
#X가 증가하는 순으로 주어짐

delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
delta_idx = 0

di, dj = delta[delta_idx]

arr = [[0] * N for _ in range(N)]

ci = 0
cj = 0
time = 0
arr[ci][cj] = 1
dir_sec = 0
apple = 0

snake = [[0, 0]]

while ci < N and cj < N:
    time += 1
    fi, fj = ci + di, cj + dj   #다음에 갈 인덱스
    
    if not (0 <= fi < N and 0 <= fj < N) or arr[fi][fj] == 1:
        break

    else:
        arr[fi][fj] = 1
        snake.append([fi, fj])  #머리 추가
        for ai, aj in pos:
            if fi == ai and fj == aj:   #사과 먹었으면
                apple = 1
                pos.remove([fi, fj])

        if not apple:   #사과 안먹었으면 꼬리 잘라냄
            tail_i, tail_j = snake.pop(0)
            arr[tail_i][tail_j] = 0

    if dir_sec < len(dir) and int(dir[dir_sec][0]) == time: #x초가 끝날 때, 방향 전환 해야함
        if dir[dir_sec][1] == 'L':  #왼쪽이면
            delta_idx = (delta_idx - 1) % 4
            di, dj = delta[delta_idx]

        elif dir[dir_sec][1] == 'D':    #오른쪽이면
            delta_idx = (delta_idx + 1) % 4
            di, dj = delta[delta_idx]
        
        dir_sec += 1


    apple = 0
    ci, cj = fi, fj

print(time)



