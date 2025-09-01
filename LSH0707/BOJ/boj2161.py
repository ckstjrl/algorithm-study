from collections import deque
N = int(input())
arr = deque(range(1, 1+N))
ans = []
while len(arr) > 1:
    ans.append(arr.popleft()) # 제거한카드 출력값에 append
    arr.append(arr.popleft()) 
ans.append(arr[0])  # 남은 카드 출력값에 append
print(*ans)