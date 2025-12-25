# BOJ2212(D3): 센서
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

# 각 센서들 간의 거리를 재고 거리가 먼 순서대로 정렬
dists = []
for i in range(N-1):
    dist = sensors[i+1] - sensors[i]
    dists.append(dist)
dists.sort(reverse=True)

# (집중국 수 - 1)개 만큼의 큰 수를 제외한 모든 거리를 더하여 출력
print(sum(dists[K-1:]))