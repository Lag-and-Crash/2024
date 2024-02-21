#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>

#define MAX_USERS 10

typedef struct
{
    char name[20];
    long age;
} User;

User *users[MAX_USERS] = {0};

void add_user()
{
    int found = -1;
    for (int i = 0; i < MAX_USERS; i++)
    {
        if (users[i] == NULL)
        {
            found = i;
            break;
        }
    }
    if (found == -1)
    {
        puts("Max capacity reached");
        return;
    }

    User *user = malloc(sizeof(User));
    printf("Name: ");
    fgets(user->name, 20, stdin);
    printf("Age: ");
    scanf("%ld", &user->age);
    getchar(); // eat newline
    users[found] = user;
    puts("User added");
}

void delete_user()
{
    int choice = -1;
    printf("Idx: ");
    scanf("%d", &choice);
    getchar(); // eat newline
    if (choice < 0 || choice >= MAX_USERS)
    {
        puts("Invalid choice");
        return;
    }
    if (users[choice] != NULL)
    {
        free(users[choice]);
    }
    puts("User deleted");
}

void view_user()
{
    int choice = -1;
    printf("Idx: ");
    scanf("%d", &choice);
    getchar(); // eat newline
    if (choice < 0 || choice >= MAX_USERS)
    {
        puts("Invalid choice");
        return;
    }
    if (users[choice] != NULL)
    {
        printf("Name: %s\nAge: %ld\n", users[choice]->name, users[choice]->age);
    }
    else
    {
        puts("User does not exist");
    }
}

void modify_user()
{
    int choice = -1;
    printf("Idx: ");
    scanf("%d", &choice);
    getchar(); // eat newline
    if (choice < 0 || choice >= MAX_USERS)
    {
        puts("Invalid choice");
        return;
    }
    if (users[choice] != NULL)
    {
        puts("New name?");
        fgets(users[choice]->name, 20, stdin);
        puts("Name changed!");
    }
    else
    {
        puts("User does not exist");
    }
}

void menu()
{
    int done = 0;
    while (!done)
    {
        puts("1. Add user\n2. View user\n3. Modify user\n4. Delete user\n5. Exit");
        int choice = 0;
        printf("> ");
        scanf("%d", &choice);
        getchar(); // eat newline
        switch (choice)
        {
        case 1:
            add_user();
            break;
        case 2:
            view_user();
            break;
        case 3:
            modify_user();
            break;
        case 4:
            delete_user();
            break;
        case 5:
            done = 1;
            break;
        default:
            puts("Invalid choice");
        }
    }
}

int main()
{
    setbuf(stdout, 0);
    char *win = malloc(1);
    win[0] = 0;
    menu();
    if (win[0] != 0)
    {
        puts("You win!");
        int fd = open("/flag.txt", O_RDONLY);
        char flag[0x50] = {0};
        read(fd, flag, sizeof(flag));
        puts(flag);
        close(fd);
    }
}