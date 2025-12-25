N = int(input())
cnt = 0
length = 1
while True:
    check = (length * (length + 1)) // 2
    if check > N:
        break
    else:
        new_N = N - check
        if new_N % length == 0:
            cnt += 1
    length += 1
print(cnt)