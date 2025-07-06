#include <iostream>
#include <climits> // for INT_MAX
using namespace std;

int main() {
    int nums[] = {12, -34, 5, 2, 1, 7};
    int size = 6;
    int smallest = INT_MAX;
    int largest = INT_MIN;

    for (int i = 0; i < size; i++) {
          smallest = min(nums[i],smallest);
          largest = max(nums [i],largest);  }
          
          
    cout << "Smallest is = " << smallest << endl;
    cout << "largest is = " << largest << endl;
    return 0;
}