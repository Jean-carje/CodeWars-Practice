#include <vector>
#include <iostream>
#include <cassert>
#include <string>

std::vector<int> digitize(unsigned long n)
{
    std::vector<int> digits;
    std::string n_in_string = std::to_string(n);

    for (std::string::size_type index = n_in_string.length(); index > 0; --index) {
        digits.push_back(std::stoi(std::string(1, n_in_string[index-1])));
    }

    return digits;
}

int main()
{
    // Run Test
    std::vector<int> result1 = digitize(348597);
    std::vector<int> expected1 = {7, 9, 5, 8, 4, 3};
    assert(result1 == expected1);

    std::vector<int> result2 = digitize(35231);
    std::vector<int> expected2 = {1, 3, 2, 5, 3};
    assert(result2 == expected2);

    std::vector<int> result3 = digitize(0);
    std::vector<int> expected3 = {0};
    assert(result3 == expected3);

    std::cout << "All tests passed successfully!" << std::endl;

    return 0;
}
