#include <iostream>
#include <vector>
using namespace std;

int main() {
	vector<int> myVector{1, 2, 3, 4, 5};
	myVector.push_back(6);

	for(int i = myVector.begin(); i != myVector.end(); ++i) {
		cout << ' ' << *i;
	}
}