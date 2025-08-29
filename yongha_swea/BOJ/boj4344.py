#Test case 의 개수가 주어진다
C = int(input())

for i in range(C):
    #주어진 Test case 의 횟수만큼 각 줄 입력 받아오기 
    arr = list(map(int, input().split()))

    #0번째 인덱스 자리는 학생 수를 지칭하지만, len을 통해서 받아오기 때문에 pop으로 빼주었다
    arr.pop(0)

    people_num = len(arr)
    score = sum(arr)

    #평균 점수 구하기
    avg = score / people_num

    count = 0.0

    #평균 값보다 점수가 높은 학생의 수 카운팅하기 
    for i in arr:
        if avg < i:
            count += 1

    #평균 값보다 높은 학생의 비율을 %로 구하고 싶은거니 *100 해주기
    above_avg = (count / people_num) * 100

    #마지막으로 소수점 3자리까지 표시
    print(f'{above_avg:.3f}%')



#아래쪽은 loop를 돌려서 접근하다가 식이 너무 복잡해져서 놓아준 케이스
    # for i in range(len(arr)):
    #     sub_num = arr[i][0]
    #     print(sub_num)
    #     score_sum = 0

    #     for j in range(1, len(arr[i])):
    #         score_sum = score_sum + arr[i][j]
    #         print(score_sum)

    #         if j == len(arr[i]-1):
    #             avg = score_sum / sub_num
    #             print(avg)
