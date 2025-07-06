#include <iostream>
#include <climits> // for INT_MAX
using namespace std;

int main() {
    int nums[] = {12, -34, 5, 2, 1, 7};
    int size = 6;
    int smallest = INT_MAX;

    for (int i = 0; i < size; i++) {
        if (nums[i] < smallest) {
            smallest = nums[i];
        }
    }

    cout << "Smallest is = " << smallest << endl;
    return 0;
}