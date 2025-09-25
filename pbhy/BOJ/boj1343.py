# 1343. 폴리오미노
'''
'.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다.
'.'는 폴리오미노로 덮으면 안 된다.
폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

[출력]
첫째 줄에 사전순으로 가장 앞서는 답을 출력한다.
만약 덮을 수 없으면 -1을 출력한다.

인덱스로 돌면서 'XXXX' 만나면 'AAAA'로 바꾸고, 인덱스 +4
'XX' 만나면 'BB'로 바꾸고, 인덱스 +2
'X'면 바꿀 게 없으니까 -1 출력 후 멈추기
'X'가 아니면('.'이면) 그냥 그대로 추가하고 인덱스 +1
'''
board = input()
idx = 0
n_board = ''
while idx<len(board):
    if board[idx:idx+4]=='XXXX':
        n_board += 'AAAA'
        idx += 4
    elif board[idx:idx+2]=='XX':
        n_board +='BB'
        idx += 2
    elif board[idx]=='X':
        n_board = -1
        break
    else :
        n_board += board[idx]
        idx += 1
print(n_board)