from collections import deque

#사다리(상승), 뱀(하락) 개수 받기
N, M = map(int, input().split())
board = list(range(101))

event = N + M

for _ in range(event):
    a, b = map(int, input().split())
    #해당 칸(값)에 착지하면 가야하는 일종의 좌표를 값으로 넣어두기
    board[a] = b

#방문 여부를 확인하기 위해서 게임맵과 동일한 칸을 가지고 있는 빈 보드 생성
visited = [0] * 101

#위치를 찍어 줄 겸 주사위 회전 수를 기록할 리스트 하나
roll = [0] * 101

#게임 시작을 0이 아닌 1로 지정
q = deque([1])

#시작 칸은 바로 방문으로 설정
visited[1] = 1

end = 100

while q:
    #현재 위치를 pop으로 빼내기
    cur = q.popleft()

    #end의 값을 도달하거나 그보다 큰 경우에는 게임 종료
    if cur >= end:
        print(roll[cur])
        break
    
    #1, 2, 3, 4, 5, 6 주사위 눈의 가능한 모든 수
    for dice in range(1, 7):
        #다음 위치는 현 위치 + 주사위 눈
        nxt = cur + dice
        #게임이 끝나지 않는 동아 계속, 100을 찍지 않는 한
        if nxt <= 100:
            nxt = board[nxt]
            #이미 방문 했을 경우에는 패스
            if not visited[nxt]:
                visited[nxt] = 1
                roll[nxt] = roll[cur] + 1
                q.append(nxt)
        else:
            #이 부분이 이해가 힘들었는데 
            #100을 넘어가는 경우에 주사위를 덜 굴리는 방법이 있다면 그걸 보기 위해서 break가 아닌 continue
            continue