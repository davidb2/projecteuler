#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

const int LIMIT = 50;
const double EPS = 0.001;

bool is_equal(double a, double b) {
    return abs(a - b) < EPS;
}

bool is_right_triangle(std::pair<double, double> a, std::pair<double, double> b, std::pair<double, double> c) {
    double dist0 = sqrt(pow(a.first - b.first, 2) + pow(a.second - b.second, 2));
    double dist1 = sqrt(pow(b.first - c.first, 2) + pow(b.second - c.second, 2));
    double dist2 = sqrt(pow(a.first - c.first, 2) + pow(a.second - c.second, 2));
    double lens[] = {dist0, dist1, dist2};
    std::sort(lens, lens+3);
    return is_equal(pow(lens[0], 2) + pow(lens[1], 2), pow(lens[2], 2));
}

int main() {
    std::vector<std::pair<double, double>> points;
    for (int x = 0; x <= LIMIT; x++) {
        for (int y = 0; y <= LIMIT; y++) {
            points.push_back(std::pair<double, double>(x, y));
        }
    }
    int ways = 0;
    std::pair<double, double> a = std::pair<double, double>(0, 0);
    for (int i = 1; i < points.size(); i++) {
        for (int j = i+1; j < points.size(); j++) {
            std::pair<double, double> b = points[i], c = points[j];
            ways += is_right_triangle(a, b, c);
        }
    }
    printf("%d\n", ways);
    return 0;
}