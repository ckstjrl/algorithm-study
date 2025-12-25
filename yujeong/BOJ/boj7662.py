# 7662. 이중 우선순위 큐

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

T = int(input())
for _ in range(T):
    k = int(input())    # 연산의 개수

    maxheap, minheap = [], []   # 최대/최소값 관리
    num_dict = dict()   # 큐에 갖고 있는 숫자별 개수 관리

    for _ in range(k):
        cmd, n = input().split()
        n = int(n)

        # 1. 삽입 연산 (I)
        if cmd == 'I':
            # if n in num_dict.keys():
            #     num_dict[n] += 1
            # else:
            #     num_dict[n] = 1
            num_dict[n] = num_dict.get(n, 0) + 1

            heappush(minheap, n)
            heappush(maxheap, -n)

        # 2. 삭제 연산 (D)
        else:
            if n == 1:  # 최댓값 삭제
                if maxheap:
                    num_dict[-maxheap[0]] -= 1

            else:       # 최솟값 삭제
                if minheap:
                    num_dict[minheap[0]] -= 1

            # num_dict에서 최댓값/최솟값 개수를 일단 감소시켰고
            # 그에 맞게 최대 힙, 최소 힙의 top 갱신 필요
            # (num_dict[top]이 0이 된 경우 pop)
            while maxheap and num_dict[-maxheap[0]] == 0:
                heappop(maxheap)
            while minheap and num_dict[minheap[0]] == 0:
                heappop(minheap)

    if minheap and maxheap:     # 큐가 비어있지 않으면 최댓값, 최솟값 출력
        print(-maxheap[0], minheap[0])
    else:                       # 아니면 'EMPTY' 출력
        print('EMPTY')