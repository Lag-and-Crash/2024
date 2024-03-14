#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

char stuff[0x100];
char * code;

void shellz(void) {
    printf("Here's your shell!\n");
    memcpy(code, stuff, 0x100); 
    typedef void (*func_t)(void);
    ((func_t)code)();
}

int main(void) {
    char buf[0x100];
    
    // Ignore this
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    code = mmap(NULL, 8192, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_ANONYMOUS|MAP_PRIVATE, -1, 0);
    
    printf("Welcome to pwn!\n");
    printf("Show me a cool exploit technique!\n");
    printf(">> ");
    fgets(stuff, 0x100, stdin);
    printf("Now tell me where to go: \n");
    printf(">> "); 
    fgets(buf, 0x200, stdin);
    return 0;
}
