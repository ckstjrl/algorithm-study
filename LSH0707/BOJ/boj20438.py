import sys
input = sys.stdin.readline
N, K, Q, M = map(int, input().split())
sleep = list(map(int, input().split()))
code = list(map(int, input().split()))
check = []
for _ in range(M):
    a, b = map(int, input().split())
    check.append([a, b])
    
arr = [0] * (N+3)  # 출석 체크 (0:결석 1:출석)

for i in code:
    if i not in sleep:  # 코드 받은 학생 중에 안자고 있으면
        x = 1
        while x * i <= N+2:  # 본인 입장 번호의 배수인 학생들 출석 처리
            arr[x * i] = 1
            x = x + 1

for j in sleep:  # 자고 있으면 결석 처리
    arr[j] = 0

for a, b in check:
    all = b - a + 1  # 구간 내 학생 수
    checked = sum(arr[a:b+1])  # 구간 내 출석한 학생 수
    print(all - checked)  # 전체 - 출석
