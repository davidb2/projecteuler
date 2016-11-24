#include <cstdio>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <climits>
#include <queue>
#include <vector>
#include <set>
#include <functional>

const char *GRID_FILE = "../pe082.txt";
const int DIMENSION = 80;
int grid[DIMENSION][DIMENSION];

void load_grid() {
    std::ifstream infile(GRID_FILE);
    int i = 0;
    while (infile) {
        std::string str;
        if (!std::getline(infile, str)) break;
        std::istringstream ss(str);
        int j = 0;
        while (ss) {
            std::string s;
            if (!std::getline(ss, s, ',')) break;
            grid[i][j++] = std::stoi(s);
        }
        i++;
    }
}

int BFS() {
    int minimum = INT_MAX;
    
    for (int i = 0; i < DIMENSION; i++) {
        std::set<std::pair<int, int>> seen;
        std::set<int> ends;
        std::priority_queue<std::pair<int, std::pair<int, int>>> pqueue;

        pqueue.push(std::pair<int, std::pair<int, int>>(-(grid[i][0]), std::pair<int, int>(i, 0)));

        while (!pqueue.empty() && ends.size() < DIMENSION) {
            std::pair<int, std::pair<int, int>> pr = pqueue.top(); pqueue.pop();
            std::pair<int, int> location = pr.second;
            int current_sum = abs(pr.first);

            if (location.second == DIMENSION - 1) {
                if (ends.find(location.first) == ends.end()) {
                    ends.insert(location.first);
                    minimum = current_sum < minimum ? current_sum : minimum;
                }
                continue;
            }

            if (seen.find(location) == seen.end()) {
                seen.insert(location);
                std::pair<int, int> dirs[3] = {
                    std::pair<int, int>(location.first - 1, location.second),
                    std::pair<int, int>(location.first + 1, location.second),
                    std::pair<int, int>(location.first, location.second + 1)
                };
                
                for (int x = 0; x < 3; x++) {
                    if (0 <= dirs[x].first && dirs[x].first < DIMENSION && 0 <= dirs[x].second && dirs[x].second < DIMENSION) {
                        pqueue.push(std::pair<int, std::pair<int, int>>(-(current_sum + grid[dirs[x].first][dirs[x].second]), dirs[x]));
                    }
                }
            }
        }
    }
    return minimum;
}

int main() {
    load_grid();
    printf("%d\n", BFS());
    return 0;
}
