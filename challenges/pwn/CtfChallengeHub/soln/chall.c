#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>

const char* challs[5] = {"pwn", "re", "misc", "forens", "crypto"};

void callme() {
  asm volatile ("pop %%rdi\n\t"
      "ret"
      :
      :
      : "rdi");
}

void pwnchall() {
    sleep(1);
    // TODO: Put pwn chall on docker instance
    puts("Error. File pwn_chall.exe was not found.");
}

void forenchall() {
    sleep(1);
    // TODO: Put memdump on docker instance
    puts("Error. File memdump.bin was not found.");
}

void miscchall() {
    char cmd[100] = {0,};
    printf("Enter cmd:\n> ");
    fgets(cmd, 0x100, stdin);
    if (strlen(cmd)) {
        puts("Command is blacklisted!");
    } else {
        puts("Popen called.\nNULL command has been executed. Result: NULL");
    }
}

void revchall() {
    char* hdigest = "a04a4032507eb242254a087f723d0a72";
    printf("MD5 Hash: %s\n", hdigest);
    puts("The flag has this MD5 hash with salt 'wakuefharkushvSERvgsdfvgSF'");
}

void cryptochall() {
    char* ct = "44476c380d5d45d358d06146472163e258b837b08ce26d253a4620e860768f8afb3badbf902ad695a4d8ff012e3386c2";
    printf("AES_ECB encrypted ciphertext: %s\n", ct);
}


int main() {
    int i,x;
    char input[1024];
    
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    
    puts("Welcome to my challenge hub! Beat one of my challenges to get the flag!");
    puts("Choose a challenge:");
    for (i=0;i<5;i++) {
        printf("%d. %s\n", i+1, challs[i]);
    }
    printf("> ");
    fgets(input, 1000, stdin);
    x = atoi(input);
    if (x == 1) {
        puts("Pwn this exe!");
        pwnchall();
    } else if (x == 2) {
        puts("Reverse this well known hashing function!");
        revchall();
    } else if (x == 5) {
        puts("Break this well known cipher with a single-known ciphertext attack!");
        cryptochall();
    } else if (x == 4) {
        puts("Find the flag in this memdump!");
        forenchall();
    } else if (x == 3) {
        puts("Get the flag in this linux jail!");
        miscchall();
    } else puts("Invalid value!");
}
