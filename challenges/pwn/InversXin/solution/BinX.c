#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
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

// Function to initialize the random number generator.
void initialize_random_seed() {
    // Use the current time as a seed for the random number generator.
    srand((unsigned int)time(NULL));
}

// Function to generate a random number in the range -100000 to 999999.
int generate_random_number() {
    // RAND_MAX is the maximum value returned by rand(). Ensure it's at least 1099999.
    if (RAND_MAX < 1099999) {
        fprintf(stderr, "RAND_MAX is too small on this system to generate the desired range.\n");
        exit(EXIT_FAILURE);
    }

    // Scale and shift the number to the desired range.
    return (rand() % 1100000) - 100000;
}


int main(){
	// Initialize the random number generator.
	initialize_random_seed();
	//Generate and print a random number.
	int random_number = generate_random_number();    
	char password[128]; // set buffer for password input
	int passcheck = 0; // init vars
	char realpass[50];
	char flag[99999];
	strcpy(realpass, readfile("pass.txt")); // cpy strings from fn to var
	printf("Password: "); // pass prompt
	gets(password); // get from input
	int result = strcmp(password, realpass); // set result
	char numinp[1000000];
	printf("What number am I thinking of: ");
	fgets(numinp, sizeof(numinp), stdin);

	int n = (int)strtol(numinp, NULL, 10);

	if (result && (n != random_number)) // if result 
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
		printf("The flag is %s\n", flag); 
	}
}

