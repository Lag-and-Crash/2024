#include <iostream>
#include <string>
using namespace std;
int main() {
    int i;
    string flag = "LMA/0v]IHV'hSfGa#aMP:Vf";
    string secrect = "IIlnvz &ows}friws";
    string input;
    cout << "\nTell me something I want to hear:\n";
    getline (cin,input);
    for(i = 0; (i < 100 && input[i] != '\0'); i++)
        input[i] = input[i] + i++;
    cout << "\nYou told me that: " << input << endl;
    if (secrect == input) {
        cout << "AWW love you too\n";
        for(i = 0; (i < 100 && flag[i] != '\0'); i++)
            flag[i] = flag[i] + i;
        cout << flag << endl;
    } else {
        cout << "That does not seem right?\n";
    }

	return 0;
}