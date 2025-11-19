'''boj7662 - 이중 우선순위 큐
이중 우선순위 큐(dual priority queue)는 전형적인 우선순위 큐처럼 데이터를 삽입, 삭제할 수 있는 자료 구조이다. 
전형적인 큐와의 차이점은 데이터를 삭제할 때 연산(operation) 명령에 따라 우선순위가 가장 높은 데이터 또는 가장 낮은 데이터 중 하나를 삭제하는 점이다. 
이중 우선순위 큐를 위해선 두 가지 연산이 사용되는데, 하나는 데이터를 삽입하는 연산이고 다른 하나는 데이터를 삭제하는 연산이다. 
데이터를 삭제하는 연산은 또 두 가지로 구분되는데 하나는 우선순위가 가장 높은 것을 삭제하기 위한 것이고 다른 하나는 우선순위가 가장 낮은 것을 삭제하기 위한 것이다.

정수만 저장하는 이중 우선순위 큐 Q가 있다고 가정하자. 
Q에 저장된 각 정수의 값 자체를 우선순위라고 간주하자.

Q에 적용될 일련의 연산이 주어질 때 이를 처리한 후 최종적으로 Q에 저장된 데이터 중 최댓값과 최솟값을 출력하는 프로그램을 작성하라.
'''
# 힙 연산 사용
# >> 힙은 최솟값 삭제가 기본값임 최댓값 삭제는?
# 힙 두개 만들어서 최댓값 연산할 힙은 -를 곱한 수를 넣어
# 최댓값 삭제 시 heappop(최댓값삭제할힙) 하고
# 최종 출력 때는 다시 -를 곱해서 출력하기
# 최댓값 삭제하면 최솟값 힙에는 숫자가 안줄어드니까 cnt 이용해서 지워졌다 치기


import sys
input = sys.stdin.readline
from heapq import heappop, heappush

T = int(input())
for _ in range(T):
    K = int(input())
    
    min_h = []  # 최소힙
    max_h = []  # 최대힙 (음수로 저장)
    visited = [False] * K  # i번째 삽입된 원소가 삭제되었는지 표시
    cnt = 0  # 삽입 순서 추적
    
    for _ in range(K):
        op, n = input().split()
        
        if op == 'I':
            num = int(n)
            heappush(min_h, (num, cnt))
            heappush(max_h, (-num, cnt))
            cnt += 1
            
        else:  # D 연산
            if op == 'D':
                if n == '1':  # 최댓값 삭제
                    while max_h and visited[max_h[0][1]]:
                        heappop(max_h)
                    if max_h:
                        n, idx = heappop(max_h)
                        visited[idx] = True
                        
                else:  # 최솟값 삭제
                    while min_h and visited[min_h[0][1]]:
                        heappop(min_h)
                    if min_h:
                        n, idx = heappop(min_h)
                        visited[idx] = True
    
    # 삭제된 원소들 정리
    while min_h and visited[min_h[0][1]]:
        heappop(min_h)
    while max_h and visited[max_h[0][1]]:
        heappop(max_h)
    
    if not min_h or not max_h:
        print("EMPTY")
    else:
        print(-max_h[0][0], min_h[0][0])