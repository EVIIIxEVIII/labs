#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int findLargestPandigit();
static int isPandigit(char* number);
int numDigits(int product);

int main() {
    int largestPandigit = findLargestPandigit();
    printf("\n");
    printf("The largest pandigital is: %d\n", largestPandigit);
    printf("\n");

    return 0;
}

int findLargestPandigit() {
    // the pandigit is a temporary storage for the concated products
    char pandigit[20];
    int pandigitLen = 0;
    pandigit[0] = '\0';

    // the buffer is used to store the temporary product as a string
    char buffer[20];
    buffer[0] = '\0';
    int largestPandigit = -1;

    for (int i = 1; i < 9999; i++) {
        for (int j = 1; j < 10;j++) {
            int product = j * i;
            int productLen = numDigits(product);

            sprintf(buffer, "%d", product);

            memcpy(pandigit + pandigitLen, buffer, productLen);
            pandigitLen += productLen;
            pandigit[pandigitLen] = '\0';

            if (pandigitLen == 9 && isPandigit(pandigit)){
                if (atoi(pandigit) > largestPandigit) largestPandigit = atoi(pandigit);
                break;
            }

            if(pandigitLen >= 9) {
                break;
            }
        }

        // use '\0' to clean the string
        // memset is not used because we will be rewriting the string anyway next iteration
        pandigit[0] = '\0';
        pandigitLen = 0;
        buffer[0] = '\0';
    }

    return largestPandigit;
}

int numDigits(int product) {
    int numbers[] = {10, 100, 1000, 10000, 100000};
    for (int i = 0; i < 5; i++) {
        if (product < numbers[i]) {
            return i+1;
        }
    }

    return 0;
}

static int isPandigit(char* number) {
    short bitmask = 0;

    for (int i = 0; i < 9; i++) {
        int digit = number[i] - '0';

        // 00000001 << 3 => 0000001000
        // 11000000 |=  0000001000 = 1100001000
        // if the digit already exists or it is equal to 0 return false
        if (bitmask & (1 << digit) || digit == 0) return 0;
        // otherwise flip the digit in the bitmask at the position of the digit
        bitmask |= (1 << digit);
    }

    return 1;
}

