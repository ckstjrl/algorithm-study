"""
BOJ14889 - 스타트와 링크

문제정의
1. N = 짝수
-> N을 스타트와 링크 팀의 N/2로 나누기
2. S[i][j] -> i와 j가 같은 팀에 속했을 때 팀에 더해지는 능력치
3. S[i][j] != S[j][i]인 경우 존재, 두 경우 모두 더해짐

로직 정의
1. dfs로 set를 활용한 조합을 설정
2. set의 len 혹은 cnt(동일함 못정함)이 N/2와 같다면 
    -> 각 set별로 값을 설정하고 abs로 차이 정해놓고 min(현재, 지금까지)로 갱신
    -> 만약에 차이가 0 이 나오면 바로 break


"""


def check(team):
    global min_sum
    teama = list(set(team))
    teamb = list(set(range(N)) - set(team))
    tempa = 0
    tempb = 0
    a = len(teama)
    b = len(teamb)
    for i in range(a-1):
        for j in range(i+1, a):
            tempa += maps[teama[i]][teama[j]]
            tempa += maps[teama[j]][teama[i]]
    
    for i in range(b-1):
        for j in range(i+1, b):
            tempb += maps[teamb[i]][teamb[j]]
            tempb += maps[teamb[j]][teamb[i]]
    diff = abs(tempb-tempa)
    min_sum = min(diff, min_sum)
    if min_sum == 0:
        return True
    else:
        return False
    

def recur(cnt, team):
    global min_sum
    # 만약 길이가 N/2 라면 recur 그만!
    if  cnt == N//2:
        if check(team):
            return min_sum
        return
    for i in range(cnt, N):
        team.append(i)
        recur(cnt+1, team)
        team.pop()
    return min_sum

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
sum_all = sum([sum(row) for row in maps])
min_sum = 99 *20
team = []
min_sum = recur(0, team)

print(min_sum)