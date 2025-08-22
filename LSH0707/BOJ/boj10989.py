import sys

input = sys.stdin.readline
count = [0] * 10001  # 카운팅 정렬(sort로 하면 에러)

N = int(input())
for _ in range(N):
    num = int(input())
    count[num] += 1

write = sys.stdout.write  # 빠른 입출력(readline, write)
for i in range(10001):
    if count[i]:
        for _ in range(count[i]):
            write(f"{i}\n")