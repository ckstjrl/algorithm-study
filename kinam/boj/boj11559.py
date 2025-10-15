'''boj11559 - Puyo Puyo

뿌요뿌요의 룰은 다음과 같다.

필드에 여러 가지 색깔의 뿌요를 놓는다. 
뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 
이때 1연쇄가 시작된다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 
터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 
이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 
상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다. 
하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 
상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

입력
총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.
R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 
즉, 뿌요 아래에 빈 칸이 있는 경우는 없다.
'''
import sys
input = sys.stdin.readline

arr = [list(input().strip()) for _ in range(12)]




di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

colors = 'RGBPY'

ans = 0

def dfs(char, ci, cj):
    stack = [(ci, cj)] # dfs용 스택
    visited[ci][cj] = 1
    puyo = [(ci, cj)] # 뿌요 터질 인덱스 담을 리스트

    while stack:
        y, x = stack.pop()
        for d in range(4):
            ni, nj = y + di[d], x + dj[d]
            if 0 <= ni < 12 and 0 <= nj < 6 and not visited[ni][nj] and arr[ni][nj] == char:
                visited[ni][nj] = 1
                stack.append((ni, nj))
                puyo.append((ni, nj))

    return puyo


def puyopuyo():
    global ans, visited
    # 전체 배열 확인해서 글자 아래에 빈공간 있으면 내려감
    while True: # 뿌요 터지는지 검사. 더이상 터질 뿌요 없으면 종료
        ispuyo = 0 # 뿌요 터졌나?
        while True: # 중력 검사. 내려갈 색깔 글자 없으면 종료
            isgravity = 0 # 내려갔나?
            for i in range(11, 0, -1): # 바닥부터 검사함
                for j in range(6):
                    if arr[i][j] == '.':
                        if arr[i-1][j] != '.': #바닥이 .인데 위가 색깔이면
                            arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
                            isgravity = 1 # 내려가는것

            if isgravity == 0: # 안내려가면? 끝
                break
        
        visited = [[0] * 6 for _ in range(12)] # 방문 배열 초기화

        for i in range(11, -1, -1):
            for j in range(6):
                if arr[i][j] != '.' and not visited[i][j]:
                    puyo_list = dfs(arr[i][j], i, j) # dfs돌아서 뿌요터질리스트 리턴
                    if len(puyo_list) >= 4: # 이어진게 4개이상이면
                        ispuyo = 1 # 뿌요 터지고
                        for i, j in puyo_list:
                            arr[i][j] = '.' # 뿌요터짐

        if ispuyo == 0: # 뿌요 안터지면 끝
            break
        
        else:
            ans += 1 

puyopuyo()
print(ans)