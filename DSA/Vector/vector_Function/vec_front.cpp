#include<iostream>
#include<vector>
using namespace std;
int main (){
          vector<int>vec;
          cout<< "size of = " << vec.size() << endl;
          vec.push_back(24);
          vec.push_back(25);
          vec.push_back(26);
          vec.push_back(27);
          
          cout<<"After push back "<< vec.size()<<endl;
          
          cout << vec.front ()<<endl;
          
          return 0;
}