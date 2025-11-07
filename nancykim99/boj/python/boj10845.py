# BOJ10845. 큐 D2

T = int(input())

q = []
for _ in range(T):
    command = list(input().split(" "))

    if command[0] == "push":
        q.append(command[1])
    elif command[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif command[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])











