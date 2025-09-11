import sys
input = sys.stdin.readline
farm = []
x = []
y = []
ex = []

k = int(input())

for i in range(6):
    dir, meter = map(int, input().split())  # 방향, 거리 입력
    farm.append([dir, meter])
    if farm[i][0] == 3 or farm[i][0] == 4:  # 세로 저장
        x.append(farm[i][1])
    if farm[i][0] == 1 or farm[i][0] == 2:  # 가로 저장
        y.append(farm[i][1])

# B의 길이 추출
for i in range(6):
    if farm[i][0] == farm[(i + 2) % 6][0]:
        ex.append(farm[(i + 1) % 6][1])

print(((max(x) * max(y)) - (ex[0] * ex[1])) * k)