
#include<iostream>
using namespace std;

int linersearch (int arr[], int size , int target){
          for (int i = 0; i < size; i++){
                    if (arr[i] == target){
                              return i;
                    }
          }
          return -1;
}
int main  (){
          int arr[] = {20,32,54,69,10,76};
          int size = 6;
          int target = 10;
          cout << linersearch (arr,size,target) <<endl ;
          return 0;
}