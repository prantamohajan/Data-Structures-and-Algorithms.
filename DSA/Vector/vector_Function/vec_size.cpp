#include<iostream>
#include<vector>
using namespace std;

int main (){
          vector<char> vec = {'a','b','c','d','e','f'};
          cout<< "size of = " << vec.size()<<endl;

          for(char val : vec){

                    cout << val<< endl;
          }
          
          return 0;
}