T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input()))
    N = len(arr)
    nara = [0] * N
    count = 0
    for i in range(N):
        if arr[i] != nara[i]:
            for j in range(i, N):
                nara[j] = arr[i]
            count += 1
   
    print(f"#{test_case} {count}")