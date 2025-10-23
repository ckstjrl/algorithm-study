j_dict = {'A':0, 'B':1, 'C':2, 'D':3,
          'E':4, 'F':5, 'G':6, 'H':7}
dirs = {'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0],
        'RT':[1,1],'LT':[1,-1],'RB':[-1,1],'LB':[-1,-1]}
king = [0] * 2
rock = [0] * 2
k, r, N = input().split()
king[0], king[1] = int(k[1])-1, j_dict[k[0]]  # 킹시작 좌표
rock[0], rock[1] = int(r[1])-1, j_dict[r[0]]  # 돌시작 좌표

def move(dir):
    nki = king[0] + dirs[dir][0]  # 다음 킹좌표
    nkj = king[1] + dirs[dir][1]
    nri = rock[0]  # 돌좌표
    nrj = rock[1]
    if nki == rock[0] and nkj == rock[1]:  # 다음킹좌표와 돌좌표가 같은 경우
        nri = rock[0] + dirs[dir][0]
        nrj = rock[1] + dirs[dir][1]
    for x in [nki,nkj,nri,nrj]:  # 다음 킹, 돌좌표가 체스판 내부인지 확인
        if 0 <= x < 8:
            continue
        else:  # 하나라도 밖이면 리턴
            return
    king[0], king[1] = nki, nkj  # 모든 좌표가 내부면 좌표값 기록
    rock[0], rock[1] = nri, nrj
    return
for _ in range(int(N)):
    move(input())
j_reverse = {0:'A', 1:'B', 2:'C', 3:'D',
             4:'E', 5:'F', 6:'G', 7:'H'}
king[0], king[1] = j_reverse[king[1]], king[0] + 1
rock[0], rock[1] = j_reverse[rock[1]], rock[0] + 1
print(king[0], end='')
print(king[1])
print(rock[0], end='')
print(rock[1])