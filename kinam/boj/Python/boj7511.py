'''boj7511 - 소셜 네트워킹 어플리케이션 

어렸을때부터 컴퓨터 프로그래밍에 엄청난 소질을 보인 상근이는 항상 소셜 네트워킹 웹사이트를 만들고 싶어 했다. 
상근이는 페이스북을 벤치마킹하기 위해 지난 3년간 열심히 사용을 했고, 
이제 페이스북의 단점을 보완한 새 소셜 네트워킹 웹 2.0 어플리케이션을 만들려고 한다.

사람들은 소셜 네트워킹 어플리케이션에 가입을 한 다음, 
현실에서 아는 사람을 친구로 추가하기 시작한다. 
이러한 친구 관계 정보를 이용해 친구 관계 그래프를 그릴 수 있다.

소셜 네트워킹 어플리케이션에서 가장 중요한 기능은 한 사람이 다른 사람의 페이지를 방문했을 때, 
친구 관계 그래프에서 두 사람 사이의 경로를 보여주는 기능이다. 
경로가 없는 경우에는 보여주지 않는다.

상근이의 서비스는 매우 유명해졌고, 
위의 기능은 사람들이 점점 많아질수록 경로를 구하는 시간이 매우 느려지게 되었다. 
그 이유는 두 사람 사이의 경로가 없는 경우에 경로를 찾기 위해 너무 오랜시간 그래프를 탐색하기 때문이었다. 
따라서, 상근이는 두 사람 사이의 경로가 존재하는지 안 하는지를 미리 구해보려고 한다.

유저의 수와 각 유저의 친구 관계가 입력으로 주어진다. 
이때, 주어지는 두 사람이 친구 관계 그래프상에서 경로가 존재하는지 안 하는지를 구하는 프로그램을 작성하시오.

'''
def find_set(x):
    # 자신 == 부모: 해당 집합의 대표자
    while x != parents[x]:
        x = parents[x]

    return x 

def union(a, b):
    parents[find_set(b)] = find_set(a)


T = int(input())
for t in range(1, T+1):
    N = int(input()) # 유저 수 N
    K = int(input()) # 친구 관계의 수 K

    # adj_list = [[] for _ in range(N)]
    parents = [i for i in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())

        # adj_list[a].append(b)
        # adj_list[b].append(a)
        union(a, b)
    M = int(input())


    ######### 직접 연결되어있는 것이 아니라 간선 연결이 되어있는지 묻는 듯 #########
    # for _ in range(M):
    #     u, v  = map(int, input().split())
    #     if v in adj_list[u]:
    #         print(f"ans 1")
    #     else:
    #         print(f"ans 0")
    ############################################################################
    friend = []
    for _ in range(M):
        u, v = map(int, input().split())
        friend.append(u)
        friend.append(v)

    print(f"Scenario {t}:")
    for i in range(0, len(friend), 2):
        if find_set(friend[i]) == find_set(friend[i+1]):
            print(1)
        else:
            print(0)

    print()

    