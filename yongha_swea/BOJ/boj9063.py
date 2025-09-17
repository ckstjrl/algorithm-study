#점의 개수
N = int(input())

dot_point = [list(map(int, input().split())) for _ in range(N)]

dot_x = []

dot_y = []

#x와y를 나눠서 리스트로 다시 정리
for i in range(N):
    dot_x.append(dot_point[i][0])
    dot_y.append(dot_point[i][1])

#최소값부터 최대값 순서로 정렬
dot_x.sort()
dot_y.sort()

#가장 큰 수 - 가장 큰 수를 통하여서 변의 길이 구하기
if len(dot_x) >= 2 and len(dot_y) >= 2:
    ans = (dot_x[-1] - dot_x[0]) * (dot_y[-1] - dot_y[0])
else:
    ans = 0

print(ans)
