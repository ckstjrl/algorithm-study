/*
BOJ1197 : 최소 스패닝 트리 (G4)

해결 방법 : MST 크루스칼 알고리즘으로 해결하기
1. 가중치를 기준으로 정렬하기
2. 사이클이 아닐 경우, union set하고 가중치를 cost에 저장해 최소비용 구하기
-> 사이클이면서 가중치 합이 최소여야 하기 때문

메모 : 
파이썬으로는 크루스칼! 하면서 풀리는게, c++로 풀려니 너무 힘들다...
*/

#include <iostream>   // cin, cout
#include <vector>     // vector
#include <algorithm>  // sort
using namespace std;

struct DSU {
  vector<int> parent, set_size; // 부모노드, 집합 크기

  DSU(int n) {
    parent.resize(n + 1); // parent vector 크기 = n+1
    set_size.assign(n + 1, 1); // set_size 크기 = n+1, 값을 모두 1로 채움
    for (int i = 1; i <= n; i++) { // parent[i] = i로 초기화 (모든 노드가 대표 노드)
      parent[i] = i;
    }
  }

  // 대표 노드 찾기
  int find_root(int x) {
    if (parent[x] == x) {
      return x;
    } else {
      return parent[x] = find_root(parent[x]); // x의 부모의 부모 -> 대표 노드까지
    }
  }

  // union 집합
  void union_set(int a, int b) {
    a = find_root(a);
    b = find_root(b);
    if (a < b) {
      parent[b] = a;
    } else {
      parent[a] = b;
    }
  }

  // 사이클 유무 확인
  bool is_cycle(int a, int b) {
    a = find_root(a);
    b = find_root(b);
    if (a == b) {
      return true;
    } else {
      return false;
    }
  }
};

struct edge {
  long long w; // 가중치
  int u, v;
};

bool sort_edge(const edge&a, const edge& b) {
  return a.w < b.w; // a의 가중치가 더 작으면 a를 앞에 두기
}

int main() {
  // 입출력 빠르게 하기
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int v, e; // 정점 개수, 간선 개수
  cin >> v >> e; 

  vector<edge> edges;

  for (int i = 0; i < e; i++) {
    int a, b;
    long long c;
    cin >> a >> b >> c;
    edges.push_back({c, a, b}); // 가중치를 앞으로
  }


  sort(edges.begin(), edges.end(), sort_edge); // 전체 가중치 기준으로 정렬

  DSU dsu(v);
  long long mst_cost = 0;

  for (int i = 0; i < e; i++) {
    int a = edges[i].u;
    int b = edges[i].v;
    long long c = edges[i].w;

    if(!dsu.is_cycle(a, b)) { // 사이클이 아닐 경우
      dsu.union_set(a, b); // union set하기
      mst_cost += c; // mst_cost에 가중치 추가
    }
  }
  cout << mst_cost;
  return 0;
};