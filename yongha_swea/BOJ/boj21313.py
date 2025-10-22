#boj21313 문어

#문어 수
octo = int(input())

hands = []

#이 부분에서 이해가 힘들었는데 결국 짝수의 경우 손 1,2만 맞닿으면 모두 손을 잡을 수 있다
for i in range(octo - 1):
    if i % 2 == 1:
        hands.append('2')
    else:
        hands.append('1')

#하지만 홀수의 경우는 3번째 손을 잡아야지 마지막 문어와 첫번째 문어의 손이 닿는다
if octo % 2 == 0:
    hands.append('2')
else:
    hands.append('3')

#마지막으로 형식에 맞춰서 다시 저장 후 출력
ans = ' '.join(hands)

print(ans)