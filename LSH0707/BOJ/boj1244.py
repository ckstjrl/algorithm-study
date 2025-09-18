N = int(input())
arr = [0] + list(map(int, input().split()))  # 스위치 번호 = 인덱스번호
S = int(input())
a = []
for _ in range(S):
    x, y = map(int, input().split())
    a.append([x, y])  # i번학생 [성별, 받은수]
def m(s):
    i = 1
    while i * s <= N:  # 스위치갯수 보다 작은 받은수의배수
        if arr[i*s] == 0:
            arr[i*s] = 1
        else:
            arr[i*s] = 0
        i = i + 1
def f(s):
    i = 0
    while True:
        if s-i-1 >= 1 and s+i+1 <= N:
            if arr[s-i-1] == arr[s+i+1]:  # 받은수 기준 좌우가 대칭인 경우
                i = i + 1  # i값 +1
            else:
                break
        else:
            break
    for a in range(s-i, s+i+1):  # 받은수 기준 i만큼 좌우
        if arr[a] == 0:
            arr[a] = 1
        else:
            arr[a] = 0
for x in a:
    if x[0] == 1:  # 남학생
        m(x[1])
    if x[0] == 2:  # 여학생
        f(x[1])
arr.pop(0)  # 0번 스위치 제거
x = len(arr) // 20  
for i in range(x+1):  # 20개씩 나누어출력
    if i != x:
        print(*arr[20*i:20*i+20])
    else:  # 20개씩 나누고 남은 것
        print(*arr[20*i:])