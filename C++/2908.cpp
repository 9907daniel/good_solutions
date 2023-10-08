#include <string>
#include <iostream>

using namespace std;

int main(){

    string x,y;

    cin >> x >> y;

    string compare_x;
    string compare_y;

    for(int i = x.size()-1 ; 0<= i; i-- ){
        compare_x += x[i];
        compare_y += y[i];
    }

    string answer;

    if (stoi(compare_x) < stoi(compare_y)){
        answer = compare_y;
    }else{
        answer = compare_x;
    }

    cout << answer;
}