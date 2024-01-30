#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* readfile(char *filename);
char* readfile(char *filename) // reading txt
{
	char * buffer = 0;
	long length;
	FILE * f = fopen(filename, "rb");
	if (f)
	{
		fseek(f, 0, SEEK_END);
		length = ftell(f);
		fseek(f, 0, SEEK_SET);
		buffer = malloc(length);
		if (buffer)
		{
			fread(buffer, 1, length, f);
		}
		fclose(f);
	}
	if (buffer)
	{
		return buffer;
	}
	else
	{
		printf("%s does not exist\n", filename);
		exit(1);
		return "";
	}
}

int main(){
	char password[128]; // set buffer for password input
	int passcheck = 0; // init vars
	char realpass[50];
	char flag[99999];
	strcpy(realpass, readfile("pass.txt")); // cpy strings from fn to var
	printf("Password: "); // pass prompt
	gets(password); // get from input
	int result = strcmp(password, realpass); // set result
	if (result) // if result 
	{
		printf("Incorrect password\n"); // print err
	}
	else // else
	{
		printf("Correct\n"); // print success
		passcheck = 1; // set result
	}
	strcpy(flag, readfile("flag.txt")); // copy flag to buffer
	if (passcheck) // if passcheck is set
	{
		printf("The flag is %s\n", flag); // display flag
	}
	return 0;
}

