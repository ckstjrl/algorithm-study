"""

"""

T = 10
for test_case in range(1, T+1):
    N = int(input())
    cal = '+-*/'
    heap = [0] * (N+1)
    for _ in range(N):
        arr = list(input().split())
        vnum = int(arr[0])
        vvlaue = [arr[1]]
        if vvlaue[0] in cal:
             vvlaue.append(int(arr[2]))
             vvlaue.append(int(arr[3]))
        else:
            vvlaue = int(vvlaue[0])
        heap[vnum] = vvlaue
    for i in range(N, 0 , -1):
        if type(heap[i]) == int:
            continue
        else:
            cur = heap[i]
            command = cur[0]
            v1, v2 = cur[1], cur[2]
            if command == "+":
                cur_v = heap[v1] + heap[v2]
            elif command == '-':
                cur_v = heap[v1] - heap[v2]
            elif command == '*':
                cur_v = heap[v1] * heap[v2]
            else:
                cur_v = heap[v1] // heap[v2]
            heap[i] = cur_v
    print(f"#{test_case} {heap[1]}")