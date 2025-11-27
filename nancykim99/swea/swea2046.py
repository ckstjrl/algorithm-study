# 주어진 숫자만큼 # 출력

N = int(input())

arr = []
for _ in range(N):
    arr += '#'

print(''.join(arr))