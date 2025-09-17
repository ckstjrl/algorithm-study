# 2953. 나는 요리사다
'''
각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다.
점수는 1점부터 5점까지 있다.
각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다.
이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.
각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

입력 리스트로 받아서 다 더하고 최댓값을 구하자.
참가자 번호는 1부터 시작하니까 winner는 인덱스니까 i+1을 해야함.
중간에 total을 초기화하면서 한 줄씩 계산할 수 있도록 하자.
'''
max_s = 0
winner = 0
for i in range(5):
    score = list(map(int, input().split()))
    total = 0   # 합 초기화 과정
    for j in range(4):
        total += score[j]
    if total > max_s:
        max_s = total
        winner = i + 1
print(winner, max_s)