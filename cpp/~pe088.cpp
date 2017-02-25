#include <iostream>
#include <cmath>
#include <set>
#include <queue>
#include <utility>
#include <vector>
#include <functional>

using namespace std;

typedef pair<int, int> P;
typedef pair<P, P> PP;

const int LIM = 10000;

int main() {
    int n; cin >> n;
    int lim = n;
    
    // (prod, sum), (curr_num, level)
    priority_queue<PP, vector<PP>, greater<PP>> bfs;
    for (int i = 1; i <= lim; i++) {
        bfs.push(PP(P(i, i), P(i, 1)));
    }

    while (!bfs.empty()) {
        PP top = bfs.top(); bfs.pop();
        int sum = top.first.first;
        int prod = top.first.second;
        int curr = top.second.first;
        int level = top.second.second;
        if (sum == prod && level == n) {
            cout << sum << endl;
            break;
        } else {
            for (int i = curr; i <= lim; i++) {
                bfs.push(PP(P(sum+i, prod*i), P(i, level+1)));
            }
        }
    }
}
