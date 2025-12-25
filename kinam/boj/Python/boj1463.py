'''boj1463 1로 만들기

정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
연산을 사용하는 횟수의 최솟값을 출력하시오.
'''
#3가지 연산을 3가지 너비로 판단
#3가지 연산의 조건이 충족되면 큐에 집어넣기
#최소 연산 = 최단거리 = BFS
N = int(input())

q = [N]
visited = [0] * (N + 1)
visited[N] = 1

while q:
    t = q.pop(0)

    if t == 1:
        print(visited[t] - 1)
        break

    for i in [t/3, t/2, t-1]:
        if int(i) == i and visited[int(i)] == 0:
            i = int(i)
            q.append(i)
            visited[i] = visited[t] + 1



