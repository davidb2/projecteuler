#include <sstream>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <memory>
#include <utility>
#include <cmath>

// Some reasoning:
// Since there is no given upper-bound of the primes,
// I decided to keep generating primes. For this, 
// since I knew prime checks were to happen in order, 
// I mantained a list of primes and just checked if the
// number in question was divisible by any of the primes.
// Furthermore, I realized I only needed to check up to the sqrt
// of the number in question. Also, I realized that if I had set 
// my own upper-bound on the primes and played a little guess and
// check, this solution would run much quicker, but that is not a
// scalable approach.
//
// While generating each prime, I extracted all of the possible patterns
// it could possibly have. For example:
//     233 => 
//         233
//         *33
//         23*
//         2*3
//         2**
// Then for each pattern, I mantained a set (or bucket) listing the
// possible digits that could replace those partiular astericks in the
// pattern.

std::vector<int> primes;

bool is_prime(int num) {
    int limit = sqrt(num);
    for (const int& prime : primes) {
        if (prime > limit) return true;
        if (num != prime && num % prime == 0) return false;
    }
    return true;
}

void possible_choices(
        const std::string& choices, 
        const int number, 
        std::string* acc,
        std::vector<std::pair<std::string, char>>* result) {
    if (number == 0) {
        result->push_back(std::pair<std::string, char>(std::string(*acc), choices[0]));
    } else {
        for (const char& choice : choices) {
            acc->push_back(choice);
            possible_choices(choices, number - 1, acc, result);
            acc->pop_back();
        }
    } 
}

void hash_choices(
        const int number, 
        std::vector<std::pair<std::string, char>>* result) {
    std::string prime_string = std::to_string(number);
    std::map<char, int> digit_counts;

    for (const char& digit : prime_string) {
        if (digit_counts.find(digit) == digit_counts.end()) {
            digit_counts[digit] = 0;
        }
        digit_counts[digit] += 1;
    }

    for (auto it = digit_counts.begin(); it != digit_counts.end(); ++it) {
        std::vector<std::pair<std::string, char>> temp_result;
        std::string acc;
        std::string choicesp(1, it->first);
        choicesp += "*";
        possible_choices(choicesp, it->second, &acc, &temp_result);
        result->insert(result->end(), temp_result.begin(), temp_result.end()); 
    }
}

std::string replace(
    const int number,
    const char digit,
    const std::string& pattern) {
  std::stringstream ss;
  std::string snumber = std::to_string(number);
  int idx = 0;

  for (const char& d : snumber) {
      ss << ((d == digit) ? pattern[idx++] : d); 
  }
  return ss.str();
}

int main(int argc, char** argv) {
    int family = 8;
    if (argc > 1) {
        family = std::stoi(argv[1]);
    }

    primes.push_back(2);

    std::map<std::string, std::unique_ptr<std::set<char>>> bucket;
    bucket["*"] = std::unique_ptr<std::set<char>>(new std::set<char>());
    bucket["*"]->insert(2);


    int n = 1;
    while (++++n) {
        if (is_prime(n)) {
            primes.push_back(n);
            std::vector<std::pair<std::string, char>> hashes;
            hash_choices(n, &hashes);
            for (auto it = hashes.begin(); it != hashes.end(); ++it) {
                char digit = it->second;
                std::string hash = replace(n, digit, it->first);
                if (bucket.find(hash) == bucket.end()) {
                    bucket[hash] = std::unique_ptr<std::set<char>>(new std::set<char>());
                }
                bucket[hash]->insert(digit);
                if (bucket[hash]->size() == family) {
                    std::cout << hash << std::endl;
                    char min = *bucket[hash]->begin();
                    std::string chash = hash;
                    std::replace(chash.begin(), chash.end(), '*', min);
                    std::cout << chash << std::endl;
                    return 0;
                }
            }
        }
    }
}
