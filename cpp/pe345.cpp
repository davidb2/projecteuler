#include <cstdio>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

const char *MATRIX_FILE = "../pe345.txt";
const int DIMENSION = 15;
const int STATES = 1 << 15;
int matrix[DIMENSION][DIMENSION];
int dp[DIMENSION][STATES];

void load_matrix() {
    std::ifstream infile(MATRIX_FILE);
    int i = 0;
    while (infile) {
        std::string str;
        if (!std::getline(infile, str)) break;
        std::istringstream ss(str);
        int j = 0;
        std::string s;
        while (ss >> s) {
            if (s[0] == '\n') break;
            matrix[i][j++] = std::stoi(s);
        }
        i++;
    }
}

void init_dp() {
    for (int i = 0; i < DIMENSION; i++) {
        for (int j = 0; j < STATES; j++) {
            dp[i][j] = -1;
        }
    }
}

int matrix_sum(int level, int state) {
    if (level == DIMENSION) {
        return 0;
    } else if (dp[level][state] == -1) {
        int max_sum = 0;
        for (int d = 0; d < DIMENSION; d++) {
            if (!((state >> d) & 1)) {
                int temp_sum = matrix[d][level] + matrix_sum(level+1, state | (1 << d));
                max_sum = temp_sum > max_sum ? temp_sum : max_sum;
            }
        }
        dp[level][state] = max_sum;
    }
    return dp[level][state];
}

int ans() {
    int max_sum = 0;
    for (int d = 0; d < DIMENSION; d++) {
        int temp_sum = matrix[d][0] + matrix_sum(1, 1 << d);
        max_sum = temp_sum > max_sum ? temp_sum : max_sum;
    }
}

int main() {
    load_matrix();
    init_dp();
    int answer = ans();
    printf("%d\n", answer);
    return 0;
}