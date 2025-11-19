arr = [list(input()) for _ in range(5)]

ans = []
cnt = 0

while cnt < 15:
    for i in range(5):
        try:
            ans.append(arr[i][cnt])
        except IndexError:
            continue
    cnt += 1

print(''.join(ans))