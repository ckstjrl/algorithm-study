'''
문제
루트 없는 트리가 주어진다.
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다.
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''



# 먼저 주어진 예제들을 다 입력받아보자.
N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    parent, child = map(int, input().split())
    adj[parent].append(child)
    adj[child].append(parent)

# 여기에 부모 정보를 저장해보자.
parent = [0] * (N + 1)

# 비어있는 큐를 만들어보자. 그리고 노드를 방문할 때, 이 큐에 같이 기록하자.
queue = [1]

# 맨 앞 원소를 꺼낸다는 의미로 index = 0 변수를 선언한 뒤 이용.
# 1번 노드부터 시작해서 자식으로 내라기며 부모를 기록.
index = 0
while index < len(queue):
    current = queue[index]
    index += 1

    # 아직 부모 노드가 정해지지 않은 노드가 있다면
    # 그 정보를 기록한 뒤, 다음에 탐색할 대상 목록에 추가하자.
    for i in adj[current]:
        if parent[i] == 0:
            parent[i] = current
            queue.append(i)

# 2번 노드부터 정답 (부모 노드) 출력.
for i in range(2, N+1):
    print(parent[i])