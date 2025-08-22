arr = list(map(str, input().split()))

#arr의 복사
arr_copy = arr[:]

#첫 자리가 1이어야지만, 순차적 증가가 가능하기 때문에 첫자리 확인 후 ascending 여부 확인
if arr[0] == '1':
    arr.sort()
    if arr == arr_copy:
        print('ascending')
    else:
        print('mixed')

#첫 자리가 8이어야지만, 순차적 감소가 가능하기 때문에 첫자리 확인 후 descending 여부 확인
elif arr[0] == '8':
    arr.sort(reverse=True)
    if arr == arr_copy:
        print('descending')
    else:
        print('mixed')

#그 외 첫자리가 어느 쪽에도 속하지 않는 경우 무조건 적으로 mixed기 때문에 else로 처리
else:
    print('mixed')
