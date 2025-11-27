# BOJ 2606. 바이러스 / D3
'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐
3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''

import sys
node = int(sys.stdin.readline())
road = int(sys.stdin.readline())
arr = [[] for _ in range(node+1)]
for _ in range(road):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b) # 이차원 배열로 서로 연결된 곳 표시
    arr[b].append(a)

visited = [0]*(node+1) # 방문했는지 확인하는 리스트
stack = [] # 스택
stack.append(1) # 스택에 1을 넣어주고 시작
visited[1] = 1 # 스택에 넣었으면 방문 체크 세트로 필수
while stack: # 스택이 비어있지 않으면 계속 돌기
    t = stack.pop(-1) #스택 뽑기
    if arr[t]: # t컴퓨터와 연결된 컴퓨터가 존재하면 if절 돌아감
        for i in arr[t]: # t컴퓨터와 연결된 컴퓨터가
            if visited[i] != 1: # 방문한 적 없는 컴퓨터라면
                stack.append(i) # 스택에 추가하고
                visited[i] = 1 # 방문도장 꾹
cnt = 0 # 감염 컴퓨터 개수 초기화
for v in visited: # 감염 컴퓨터 찾기
    if v == 1:
        cnt += 1
print(cnt-1) # 1번 컴퓨터는 제외해야하므오 -1해주기