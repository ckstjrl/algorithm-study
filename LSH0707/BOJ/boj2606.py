V = int(input())
E = int(input())
A = {}
for i in range(V):  
    A[i+1] = []
for _ in range(E):  # 각 컴퓨터랑 연결된 컴퓨터 딕셔너리
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
visited = [0] * (V + 1)
visited[1] = 1  # 초기화
stack = []
stack.extend(A[1])
while stack:
    a = stack.pop()
    if visited[a] == 0:  # 바이러스 걸린 적 없으면 감염시키고 연결된 컴퓨터 stack에 추가
        visited[a] = 1
        stack.extend(A[a])
print(sum(visited)-1)  # 1번컴퓨터는 포함 x
    