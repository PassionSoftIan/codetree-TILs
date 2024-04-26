#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    float ft = 30.48;

    float a;
    cin >> a;

    cout << fixed;
    cout.precision(1);
    
    cout << a*ft;

    return 0;
}