#include <iostream>
using namespace std;
int sum(int a, int b);
int main()
{
    int a, b, c;
    cout << "enter the value of a";
    cin >> a;
    cout << "enter the value of b";
    cin >> b;
    sum(a, b);
}
int sum(int a, int b)
{
    int c = a + b;
    cout << "the value of the sum is" << c;
}