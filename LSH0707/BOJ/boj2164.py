from collections import deque
N = int(input())
arr = deque(range(1, N + 1))
while len(arr) > 1:
    arr.popleft()
    arr.append(arr.popleft())  # arr의 길이가 1이 될때까지 실행
print(arr[0])