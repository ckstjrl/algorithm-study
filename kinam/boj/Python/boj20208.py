'''boj20208 - 진우의 민트초코우유

진우는 민트초코우유를 좋아하는 민초단이다. 
힘든 일이 있더라도 민트초코우유 하나를 마시면 기운이 펄펄 솟는다고 한다!

민트초코우유를 너무 좋아하는 나머지 진우는 매일 아침 특정 지역들에서 민트초코우유가 배달된다는 N × N 크기의 2차원 민초마을로 이사를 하였다.

진우는 아침에 눈을 뜨면 집에서 민초마을의 지도를 들고 민트초코우유를 찾으러 출발한다. 
이때의 초기 체력은 M이다. 
여기에서 체력은 진우가 이동할 수 있는 거리를 나타낸다. 
진우는 지도상에서 상, 하, 좌, 우로 1칸씩 이동할 수 있으며 이동하면 체력이 1만큼 줄어든다. 
진우가 마을을 돌아다니다가 민트초코우유를 마신다면 체력이 H 만큼 증가하며 진우의 체력이 초기체력 이상으로 올라갈 수 있다. 
체력이 0이 되는 순간 진우는 이동할 수 없다.

민트초코를 찾으러 돌아다니다가 마을 한복판에서 체력이 0이 되어 집으로 못 돌아가는 상황은 만들어져서는 안된다. 
진우가 얼마나 많은 민트초코우유를 마시고 집으로 돌아올 수 있는지 알아보자.'''

# cnt가 줄어드는 BFS?
# 집에서 모든 우유까지의 delta x ,delta y 합을 구하기?
# 남은 체력 이내면 BFS나 DFS수행하기
import sys
sys.setrecursionlimit(10**5)


N, M, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

#우유, 집 위치 찾기
milk = []
home = None

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            milk.append((i, j))
        
        elif arr[i][j] == 1:
            home = (i, j)

max_milk = 0

visited = set()

def dfs(current_i, current_j, current_hp, visited_milk, milk_cnt):
    global max_milk

    #집까지 갈 수 있으면 우유 최대치 갱신
    home_dist = abs(current_i - home[0]) + abs(current_j - home[1])
    if current_hp >= home_dist:
        max_milk = max(max_milk, milk_cnt)


    # 다음에 갈 우유 찾기
    for idx, (ni, nj) in enumerate(milk):
        if idx not in visited_milk:
            dist = abs(current_i - ni) + abs(current_j - nj)
            if dist <= current_hp: #현재 체력으로 갈 수 있으면
                visited_milk.add(idx)
                dfs(ni, nj, current_hp - dist + H, visited_milk, milk_cnt + 1)
                visited_milk.remove(idx)

dfs(home[0], home[1], M, visited, 0)

print(max_milk)