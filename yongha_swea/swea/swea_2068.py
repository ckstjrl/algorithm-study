T = int(input())

for tc in range(1, T+1):
    #10개의 수의 배열을 리스트 형태로 받기
    arr = list(map(int, input().split()))

    #작은 수부터 순차적으로 나열
    arr.sort()

    #print를 하는 동시에 라스트의 가장 마지막 수를 출력
    print(f'#{tc} {arr[-1]}')