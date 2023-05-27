#include <iostream>

using namespace std;


int sum0(int x) {
    return x;
}


int sum(int a, int b)
{
    int x = sum0(a);
    return x + b;
}


char str(char x) {
    return x;
}


void func() {
    cout << "I'm function" << endl;
}


void func1()
{
    for (int i = 0; i < 21; i++) {
        cout << "I is: " << i << "\n";
    }
}


void loop()
{
    for (int i = 100; i > 0; i--) {
        cout << "Second I is: " << i << "\n";
    }
}


void func2() {
    cout << "Enter a symbol: " << endl;
}


void busters() {
    cout << "It isn't your business!" << endl;
}


char input() 
{
    char s;
    cin >> s;
    return s;
}


void out()
{
    int x = sum(10, 20);
    char s = input();
    char st = str(s);
    cout << st << ": " << x << endl;
}


int main()
{
    func();
    func1();
    loop();
    func2();
    out();
    busters();
    return 0;
}


