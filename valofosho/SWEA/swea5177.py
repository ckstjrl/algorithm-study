"""
이진 최소힙은 다음과 같은 특징을 가진다.

    - 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.

    - 부모 노드의 값<자식 노드의 값을 유지한다. 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.

    - 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가한다.

예를 들어 7, 2, 5, 3, 4, 6이 차례로 입력되면 다음과 같은 트리가 구성된다.

들어온 순서에 따라서 부모 체크 하면서 


하나가 들어오면
부모가 있는지 체크하고
부모가 있으면
부모와의 사이즈 비교
부모가 크면 부모랑 바꾸기
부모가 작으면 그대로 두기

자식 노드의 값이 부모 노드보다 크면 자리를 바꿔준다


"""
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and  heap[c] < heap[p]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    heap = [0] * 10000001
    arr = list(map(int, input().split()))
    last = 0
    for num in arr:
        enq(num)
    a  = N//2
    cnt = 0
    while a:
        cnt += heap[a]
        a //= 2
    print(f"#{test_case} {cnt}")
