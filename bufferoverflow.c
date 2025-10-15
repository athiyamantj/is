#include <stdio.h>
#include <string.h>

void bufferoverflow(void) {
    char buffer[16];               
    unsigned int secret = 0x11223344; 
    char input[256];

    printf("Enter some text (longer than 16 chars to overflow):\n");
    if (!fgets(input, sizeof(input), stdin)) return;

    input[strcspn(input, "\n")] = '\0';

    printf("Before copy: buffer_size=%zu, input_length=%zu, secret=0x%08X\n",
           sizeof(buffer), strlen(input), secret);

    strcpy(buffer, input);

    printf("After copy (showing up to 16 bytes): %.16s\n", buffer);
    printf("Secret value now: 0x%08X\n", secret);
}

int main(void) {
    bufferoverflow();
    return 0;
}
