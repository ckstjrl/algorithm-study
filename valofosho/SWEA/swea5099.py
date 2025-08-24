"""
피자는 1번 위치에서 부터 뺀다
1번에서 치즈 있으면 N//2 하고 다시 넣고
치즈가 0이 되면 화덕에서 꺼내고 그 자리에 남은 피자를 넣는다.

로직 정의
1. N개의 피자판에 일단 넣는다
2. N 개의 피자 중에서 1 마다 N//2 연산 수행
3. 만약 0이 된 값이 있으면 그자리에서 pop
4. 빈자리는 기존 어레이에서 하나씩 넣어준다?
"""
from collections import deque
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    pizzas = deque()
    cooked = []
    # [[인덱스, 치즈양], [인덱스, 치즈양]] 으로 만들어주기
    for idx, pizza in enumerate(arr):
        pizzas.append([idx+1, pizza])
    oven = deque()
    for i in range(N):
        # 오븐에 가능한 수만큼 먼저 초기로 채워주기
        oven.append(pizzas.popleft())
    
    while oven:
        cur = oven.popleft()
        cur[1] = cur[1] // 2
        if cur[1]:
            oven.append(cur)
        else:
            cooked.append(cur[0])
            # 남은 피자가 있다면
            if pizzas:
                # 피자 목록에서 좌측 값 넣어주기
                oven.append(pizzas.popleft())
            else:
                continue    
    
    print(f"#{test_case} {cooked[-1]}")