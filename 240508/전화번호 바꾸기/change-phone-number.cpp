#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    string input;
    
    getline(cin, input);

    string s, m, e;

    stringstream ss(input);

    getline(ss, s, '-');
    getline(ss, m, '-');
    getline(ss, e);

    cout << s << "-" << e << "-" << m;

    return 0;
}