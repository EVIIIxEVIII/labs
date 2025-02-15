#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void findLargestPandigit(int* number);
static void isPandigit(char* number, int* res);
void numDigits(int product, int* res);

int main() {
    int largestPandigit = 0;
    // pass a pointer to the location which will store the result of the computation
    findLargestPandigit(&largestPandigit);

    printf("\n");
    printf("The largest pandigital is: %d\n", largestPandigit);
    printf("\n");

    return 0;
}

void findLargestPandigit(int* number) {
    char pandigit[20];
    int pandigitLen = 0;
    pandigit[0] = '\0';

    char buffer[20];
    buffer[0] = '\0';
    int largestPandigit = -1;

    for (int i = 1; i < 9999; i++) {
        for (int j = 1; j < 10;j++) {
            int product = j * i;
            int productLen = 0;
            numDigits(product, &productLen);

            sprintf(buffer, "%d", product);

            memcpy(pandigit + pandigitLen, buffer, productLen);
            pandigitLen += productLen;
            pandigit[pandigitLen] = '\0';

            int isPand = 0;
            isPandigit(pandigit, &isPand);

            if (strlen(pandigit) == 9 && isPand){
                if (atoi(pandigit) > largestPandigit) largestPandigit = atoi(pandigit);
                break;
            }

            if(strlen(pandigit) >= 9) {
                break;
            }
        }

        pandigit[0] = '\0';
        pandigitLen = 0;
        buffer[0] = '\0';
    }

    *number = largestPandigit;
}

static void isPandigit(char* number, int* res) {
    short bitmask = 0;

    for (int i = 0; i < 9; i++) {
        int digit = number[i] - '0';

        if (bitmask & (1 << digit) || digit == 0) {
            *res = 0;
            return;
        }
        bitmask |= (1 << digit);
    }

    *res = 1;
}

void numDigits(int product, int* res) {
    int numbers[] = {10, 100, 1000, 10000, 100000};
    for (int i = 0; i < 5; i++) {
        if (product < numbers[i]) {
            *res = i+1;
            return;
        }
    }

    *res = 0;
}

