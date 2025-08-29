# BOJ2161. 카드1

N = int(input())

deck = []
for i in range(1, N+1):
    deck.append(i)

ans = []
while len(deck) != 0:
    if len(deck) == 0: # 
        break
    floor = deck.pop(0) # 하나는 버리고
    ans.append(str(floor))
    if len(deck) == 0:
        break
    below = deck.pop(0) # 하나는 밑으로 옮기기
    deck.append(below) # 가장 뒤로 옮기기


print(' '.join(ans))






