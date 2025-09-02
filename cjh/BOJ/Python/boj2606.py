n = int(input())
status = [0]*n
n_edge = int(input())

for i in range(1, n_edge+1):
    edge = list(map(int, input().split()))
    n1 = edge[0]-1
    n2 = edge[1]-1

    if status[n1] == 0 and status[n2] == 0:
        status[n1] = i
        status[n2] = i
    elif status[n1] != 0 and status[n2] == 0:
        status[n2] = status[n1]
    elif status[n1] == 0 and status[n2] != 0:
        status[n1] = status[n2]
    else:
        temp = status[n1]
        for j in range(n):
            if status[j] == temp:
                status[j] = status[n2]
    # print(status)
cnt = 0
for i in range(1, n):
    if status[i] == status[0]:
        cnt += 1
print(cnt)