// g++ src.cpp -fpie -fstack-protector -o lucky_plaza

#include <iostream>
#include <vector>

using namespace std;

void add_lucky_number(vector<long> &vec)
{
    if (vec.size() > 88)
    {
        cout << "Too many numbers!\n";
        return;
    }

    int number = 0;
    cout << "Add your lucky number!\n";
    cin >> number;
    vec.push_back(number);
    cout << "Added!\n";
}

void view_lucky_number(vector<long> &vec)
{
    cout << "Which lucky number do you want to view?\n";
    size_t idx = 0;
    cin >> idx; // 1-index
    if (idx - 1 >= vec.size())
    {
        cout << "You don't have enough lucky numbers...\n";
        return;
    }
    cout << "Lucky number " << idx << ": " << vec[idx - 1] << '\n';
}

void modify_lucky_number(vector<long> &vec)
{
    cout << "Which lucky number do you want to modify?\n";
    size_t idx = 0;
    cin >> idx; // 1-index
    if (idx - 1 >= vec.size())
    {
        cout << "You don't have enough lucky numbers...\n";
        return;
    }
    cout << "What value do you want to set it to?\n";
    long value = 0;
    cin >> value;
    vec[idx - 1] = value;
    cout << "Updated!\n";
}

void guess_lucky_number(vector<long> &vec)
{
    int guess = 0;
    int correct = rand() % 0x88;
    cout << "Guess: ";
    cin >> guess;
    if (guess == correct)
    {
        cout << "Lucky you!\n";
        vec.pop_back();
    }
    else
    {
        cout << "Oops, try again!\n";
    }
}

bool menu(vector<long> &vec)
{
    cout << "1. Add lucky number\n2. View lucky number\n3. Modify lucky number\n4. Guess lucky number\n5. Exit\n";
    cout << "Choice: ";
    int choice = 5;
    cin >> choice;
    switch (choice)
    {
    case 5:
        cout << "Goodbye!\n";
        return false;
    case 1:
        add_lucky_number(vec);
        break;
    case 2:
        view_lucky_number(vec);
        break;
    case 3:
        modify_lucky_number(vec);
        break;
    case 4:
        guess_lucky_number(vec);
        break;
    }

    return true;
}

class Person
{
    vector<long> *my_vec;
    string name;

public:
    Person(string name, vector<long> *vec) : name(name), my_vec(vec) {}
};

void setup()
{
    srand(time(0));
}

int main()
{
    setup();
    Person *person = nullptr;
    vector<long> vec;
    vec.push_back(42);

    string name;
    cout << "Your name: ";
    cin >> name;
    person = new Person(name, &vec);

    std::cout << "🍀 Lucky Plaza 🍀\n";
    while (menu(vec))
        ;
}