'''boj2606 바이러스
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 
연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 
2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''
# DFS or BFS 사용
# visited 방문 배열 만들고 방문한 곳은 1로 표시
# 최종적으로 sum(visited) 하면 될듯

N = int(input())
connected = int(input())
computer = [[] for _ in range(N+1)]

for i in range(connected):
    v1, v2 = map(int, input().split())
    computer[v1].append(v2)
    computer[v2].append(v1)

# print(f"computer : {computer}")
# computer.sort(key=lambda x:x[0]) # 1에서 시작하도록 정렬
# computer : [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# 1번은 2 5 와 연결, 2번은 1 3 5와 연결...
q = [1]
visited = [0] * (N+1)
visited[1] = 1 

while q:
    t = q.pop(0)

    for i in computer[t]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = 1

print(sum(visited)-1)


