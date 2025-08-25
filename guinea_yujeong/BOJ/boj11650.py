import sys  #표준 입출력을 빠르게 다루기 위해 사용
input = sys.stdin.readline

n = int(input())

points = []   #각 점을 [x,y] 형태로 담을 컨테이너
for i in range(n):
    point = list(map(int, input().split()))

    points.append(point)
points.sort(key = lambda x: (x[0], x[1]))

for p in points:
    print(*p)