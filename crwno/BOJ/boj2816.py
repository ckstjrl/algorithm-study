N = int(input())
channel = [input() for _ in range(N)]
ans = []
for i in range(N):
    if channel[i] == 'KBS1':
        ans += '1' * i
        ans += '4' * i
        index = i
        break
for i in range(N):
    if channel[i] == 'KBS2':
        if i < index:
            ans += '1' * (i + 1)
            ans += '4' * i
        else:
            ans += '1' * i
            ans += '4' * (i - 1)
        break
print(''.join(ans))