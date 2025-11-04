# 2212. 센서

N = int(input())    # 센서 개수 
K = int(input())    # 집중국 개수 
sensor = list(map(int, input().split()))
sensor.sort()   # 센서 위치를 정렬

diff = []       # 센서 간 간격을 차례로 저장할 리스트
for i in range(N-1):
    diff.append(sensor[i+1] - sensor[i])

diff.sort()     # 최솟값을 구하기 위해 센서 간 간격 정렬

# 센서 간 간격 N-1개 중, 
# 집중국 K개 간의 거리 K-1개는 수신 가능 영역이 아닐 수밖에 없음
# 이걸 제외한 나머지 거리 합 = 집중국의 수신 가능영역 거리 합 
ans = sum(diff[:(N-K)]) 
print(ans)