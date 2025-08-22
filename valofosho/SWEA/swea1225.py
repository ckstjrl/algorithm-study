"""
n개의 수를 처리하면 8자리 암호 생성
- 8 개의 숫자 입력
- 첫 번째 숫자 1감소 -> 맨 뒤로
- 다음 첫 번째는 2 감소, -> 맨뒤
- 이걸 한 사이클
- 한 번이라도 0되면 0으로 유지 + 
"""

from collections import deque
for test_case in range(10):
    T = int(input())
    arr = deque(map(int, input().split()))
    flag = True
    while flag:
        for i in range(5):
            cur = arr.popleft()
            cur -= i+1
            if cur > 0:
                arr.append(cur)
            else:
                cur = 0
                arr.append(cur)
                flag = False
                break
    print(f"#{T}", end=' ')
    print(*arr)