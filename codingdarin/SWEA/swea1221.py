#swea 1221. GNS (D3)

T = int(input())
for tc in range(1, T+1):
    tn, N = input().split()
    N = int(N)
    arr = input().split()

    # ----------------------------------------------3회차 풀이

    eng = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    newlist = [] # 순차 정렬에 쓸 빈 리스트 생성
    
    #각 값에 맞는 숫자(인덱스) 연결을 위한 이뉴머레이트 함수 사용
    for i, value in enumerate(eng): 
        for j in range(N):
            if str(arr[j]) == value:
                newlist.append(value) #인덱스 순서로 추가

    print(tn)
    print(*newlist)


    # ----------------------------------------------2회차 풀이

    # eng = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # num_sort = ['0','1','2','3','4','5','6','7','8','9']
    #
    # for i in range(N):
    #     for j in range(10):
    #         if arr[i] == eng[j]:
    #             arr[i] = num_sort[j]
    #
    # arr = list(map(int, arr))
    # arr.sort()
    # arr = list(map(str, arr))
    #
    # for i in range(N):
    #     for j in range(10):
    #         if arr[i] == num_sort[j]:
    #             arr[i] = eng[j]
    #
    #
    # print(tn)
    # print(*arr)


     # ----------------------------------------------1회차 풀이
     #
     #  
     #    arr2 = [''] * N
     #
     #    for i in range(N):
     #        if arr[i] == 'ZRO': arr2[i] = '0'
     #        elif arr[i] == 'ONE': arr2[i] = '1'
     #        elif arr[i] == 'TWO': arr2[i] = '2'
     #        elif arr[i] == 'THR': arr2[i] = '3'
     #        elif arr[i] == 'FOR': arr2[i] = '4'
     #        elif arr[i] == 'FIV': arr2[i] = '5'
     #        elif arr[i] == 'SIX': arr2[i] = '6'
     #        elif arr[i] == 'SVN': arr2[i] = '7'
     #        elif arr[i] == 'EGT': arr2[i] = '8'
     #        elif arr[i] == 'NIN': arr2[i] = '9'
     #
     #    arr2 = list(map(int, arr2))
     #    arr2.sort()
     #    arr2 = list(map(str, arr2))
     #
     #    for i in range(N):
     #        if arr2[i] == '0': arr[i] = 'ZRO'
     #        elif arr2[i] == '1': arr[i] = 'ONE'
     #        elif arr2[i] == '2': arr[i] = 'TWO'
     #        elif arr2[i] == '3': arr[i] = 'THR'
     #        elif arr2[i] == '4': arr[i] = 'FOR'
     #        elif arr2[i] == '5': arr[i] = 'FIV'
     #        elif arr2[i] == '6': arr[i] = 'SIX'
     #        elif arr2[i] == '7': arr[i] = 'SVN'
     #        elif arr2[i] == '8': arr[i] = 'EGT'
     #        elif arr2[i] == '9': arr[i] = 'NIN'
     #
     #    print(f"#{tc} ")
     #    print(*arr)


