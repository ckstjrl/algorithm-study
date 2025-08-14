#8을 입력시에 8 7 6 5 ...

key = int(input())

ans = []

str_ans = ''

while key != -1:
    ans.append(str(key)) #0까지 출력, 그 다음 -1을 찍기 때문에 다음 순회에서 중단
    key = key -1 #매 순회마다 1씩 수를 낮추기

str_ans = ' '.join(ans) #join을 통해 중간에 띄워쓰기 추가

print(f'{str_ans}')