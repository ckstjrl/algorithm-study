'''보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.


10 1 9 2 8 3 7 4 6 5


주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오'''

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    #리스트의 가장 큰 수 찾아서 반환
    #작은수 찾아서 제거반환 반복

    result = []
    while len(arr) > 0: #arr의 요소들 제거해서 최종적으로 빈 리스트가 되면 끝
        max_arr = arr[0]
        min_arr = arr[0]
        max_idx = 0
        min_idx = 0

        for i, v in enumerate(arr):
            if max_arr < v:
                max_arr = v

            if min_arr > v:
                min_arr = v


        max_idx = arr.index(max_arr) #가장 큰 값의 인덱스 값을 반환함
        result.append(arr.pop(max_idx)) #가장 큰 값을 제거 후 반환

        min_idx = arr.index(min_arr) #가장 작은 값의 인덱스 값을 반환
        result.append(arr.pop(min_idx)) # 가장 작을 값을 제거 후 반환

    print(f"#{t}", *result[:10])
