//using a liner search find the are target 8 

# include<iostream>
using namespace std;

int linearSearch(int arr[], int size, int target){
          for(int i = 0; i < size; i++){
                    if(arr[i] == target){
                              return i;
                    }
          }
          return -1;
}
int main (){
          int arr[]={4,8,5,6,9,4,78};
          int size = 7;
          int target = 78;
          cout << linearSearch (arr, size, target ) <<endl;
          return 0;
}