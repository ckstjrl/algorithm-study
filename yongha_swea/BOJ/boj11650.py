#기능은 구현했지만, 시간 초과로 풀이 실패

#N번 만큼의 점을 받기
N = int(input())

#각 점의 x,y 좌표를 기록할 리스트
x = []
y = []

#들어오는 값을 x와 y로 나눠서 받고 각 리스트에 넣어주기
for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

#정렬
x.sort()

y.sort()

#오름차순으로 정렬된 값을 하나씩 x와y pair로 출력
for i in range(N):
    print(f'{x[i]} {y[i]}')