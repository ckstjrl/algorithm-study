T = int(input())
for tc in range(1, T + 1):
    arr = list(map(str, input()))
    score = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            count += 1
        else:
            count = 0
        score += count
    print(score)