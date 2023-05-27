#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;


int input()
{
	cout << "X: ";
	int x;
	cin >> x;
	return x;
}


void loop()
{
	int x = input();
	for (int i = 0; i < 100; i++) {
		if (i == 10) {
			cout << "I is: " << i << endl;
		}

		else if (i == 20) {
			cout << "I is: " << i << endl;
		}

		else if (i == x) {
			cout << "I " << "(" << i << ") " << "is equal to X " << "(" << x << ")" << endl;
		}
	}
}


void str()
{
	cout << "Enter your string: ";
	string s;
	cin >> s;
	cout << "Your string is: " << s << endl;
}

void str1()
{
	string nazv_sh;
	cout << ": ";
	getline(cin, nazv_sh);
}

void main() 
{
	loop();
	str();
	//str1();
}