def last_card(N):
    queue = [0] * (N + 1)  # 원형 큐
    front, rear = 0, 0

    # 큐 초기화: 1 ~ N
    for i in range(1, N + 1):
        rear = (rear + 1) % (N + 1)
        queue[rear] = i

    # 카드가 한 장 남을 때까지 반복
    while (front + 1) % (N + 1) != rear:

        # 1. 맨 위의 카드 버리기 (dequeue)
        front = (front + 1) % (N + 1)

        # 2. 맨 위의 카드를 맨 아래로 옮기기 (dequeue 후 enqueue)
        front = (front + 1) % (N + 1)
        card = queue[front]
        rear = (rear + 1) % (N + 1)
        queue[rear] = card

    # 큐의 마지막에 남은 카드 한 장에 적힌 숫자를 반환
    return queue[rear]

N = int(input())
print(last_card(N))