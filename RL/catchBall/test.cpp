#include <iostream>

using namespace std;

int main() {
    for (int i = 0; i < 10000000; ++i) {
        // cout << i << '\r';
        cout << i << '\r' << flush;
        for (int j = 0; j < 10000000; ++j) ;
    }
}
