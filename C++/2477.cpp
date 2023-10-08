#include <string>
#include <iostream>

int a,b,c;
int multiplied;
int l[10] = {0,};

using namespace std;

int main(){
    cin >> a >> b >> c;

    multiplied = a*b*c;

    string converted = to_string(multiplied);

    for(int i=0; i< converted.size(); i++){
        
        if(isdigit(converted[i])){
            int tmp = converted[i]-'0';
            l[tmp] += 1;
        }
    }

    for(int i=0; i< 10; i++){
        cout << l[i] << endl;
    }
}