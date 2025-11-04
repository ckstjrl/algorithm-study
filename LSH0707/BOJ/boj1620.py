N, M = map(int, input().split())
arr = [0]
d = {}
for i in range(N):  # 포켓몬 번호(리스트 인덱스), 포켓몬 이름(리스트)
    a = input()
    arr.append(a)
for i in range(len(arr)):  # 딕셔너리{포켓몬 이름: 포켓몬 번호}
    d[arr[i]] = i
for _ in range(M):
    b = input()
    if b.isdigit() is True:  # 번호입력 이름출력
        print(arr[int(b)])
    else:
        print(d[b])  # 이름입력 번호출력