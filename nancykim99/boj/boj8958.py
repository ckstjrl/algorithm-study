# BOJ8958. OX퀴즈 D1

T = int(input())
for _ in range(T):
    arr = list(input())

    relay_arr = []
    cnt_relay = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt_relay += 1
            relay_arr.append(cnt_relay)
        if arr[i] == 'X':
            cnt_relay = 0

    ans = sum(relay_arr)
    print(ans)








