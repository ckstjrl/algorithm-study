"""
회의실 배정
N <- 회의 개수
I(s,e) <- 회의 시작 끝
끝과 동시에 시작 가능
시작은 반드시 끝보다 작기 때문에 끝이 작은 순으로 sort
"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
meeting = sorted(arr, key= lambda x: (x[1],x[0]))
temp = 0
max_meet = 0
for start, end in meeting:
    if start >= temp:
        temp = end
        max_meet += 1
print(max_meet)
