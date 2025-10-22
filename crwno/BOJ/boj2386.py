while True:
    arr = input()
    if arr == '#':
        break
    cnt = -1
    for i in arr:
        if i.lower() == arr[0] or i.upper() == arr[0]:
            cnt += 1
    print(f'{arr[0]} {cnt}')