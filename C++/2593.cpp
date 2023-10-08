#include <string>
#include <iostream>

using namespace std;

int l[1001] = {0,};
int tmp = 0;
int chebin = 0;
int total = 0;
int maxCount = 0;

int main(){

    for(int i=0; i<10; i++){
        cin >> tmp;
        l[tmp] += 1;
        total += tmp;
    }

    for(int i=0; i< 1001; i++){
        if (l[i] > maxCount){
            maxCount = l[i];
            chebin = i;
        } 
    }

    cout << total/10 << endl;
    cout << chebin << endl;

}