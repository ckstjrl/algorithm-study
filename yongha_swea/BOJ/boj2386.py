#BOJ2386 도비의 영어 공부

running = True

while running:
    arr = ''
    arr = input()
    
    # '#'이 input으로 들어오는 순간 loop 깨기, 종료
    if arr == '#':
        break
    
    #모든 문자를 찾아주기 위해서 전부 소문자로 변환
    lower_arr = arr.lower()

    key_letter = lower_arr[0]

    count = 0
    
    # 타켓 철자가 나올때마다 1씩 카운트 더하기 (첫번째는 무조건 본인이 나오기 때문에 1 마지막에 빼기)
    for i in lower_arr:
        if i == key_letter:
            count += 1

    print(f'{key_letter} {count-1}')
