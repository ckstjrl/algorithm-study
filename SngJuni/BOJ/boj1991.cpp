#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map<char, pair<char, char>> graph;

void preorder(char root, unordered_map<char, pair<char, char>>& graph) {
    if (root == '.') return;

    cout << root;
    preorder(graph[root].first, graph);
    preorder(graph[root].second, graph);
}

void inorder(char root, unordered_map<char, pair<char, char>>& graph) {
    if (root == '.') return;
    
    inorder(graph[root].first, graph);
    cout << root;
    inorder(graph[root].second, graph);
}

void postorder(char root, unordered_map<char, pair<char, char>>& graph) {
    if (root == '.') return;
    
    postorder(graph[root].first, graph);
    postorder(graph[root].second, graph);
    cout << root;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    char root, left, right;
    for (int i = 0; i < N; i++) {
        cin >> root >> left >> right;
        graph[root] = {left, right};
    }
    
    root = 'A';
    preorder(root, graph);
    cout << '\n';
    inorder(root, graph);
    cout << '\n';
    postorder(root, graph);

    return 0;
}