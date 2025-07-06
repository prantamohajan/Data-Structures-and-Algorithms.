#include<iostream>
using namespace std;

int main (){
          int i;
          int size = 5;
          int marks[size];

          for(i = 0; i<size; i++){
                    cin>> marks[i];
          }
          for(i = 0; i<size; i++){
                    cout<<marks[i]<<endl;
          }

}