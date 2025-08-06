T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_list= arr.copy()
    check = [0] * 51
    # 카운팅 정렬 활용
    for i in range(len(arr)):
        check[arr[i]] += 1
    for i in range(1, 51):
        check[i] += check[i-1]
    for i in range(N-1, -1, -1):
        check[arr[i]] -= 1
        sorted_list[check[arr[i]]] = arr[i]
    # 문자열 리스트로 변환 및 출력
    new_list= list(map(str, sorted_list))
    ans = ' '.join(new_list)
    print(f"#{test_case} {ans}")