#include <string>
#include <iostream>
#include <list>

int l[10];
int in, out;
int current_max = 0;
int tmp = 0;

using namespace std;

int main(){
    for(int i=0; i < 10; i++){
        
        cin >> out >> in;
        
        tmp += in;
        tmp -= out;

        current_max = max(current_max, tmp);
    }

    cout << current_max;

}
