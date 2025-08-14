T = int(input())
for tc in range(1, T + 1):
    word = input()
    mid = len(word) // 2

    # "왼쪽 반 == 오른쪽 반" 이라면, 1 출력
    if word[:mid] == word[-1:-1 - mid:-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')