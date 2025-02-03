#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int findLargestPandigit();
int isPandigit(char* number);

int main() {
    printf("\n");
    findLargestPandigit();

    return 0;
}

int findLargestPandigit() {
    char pandigit[20];
    pandigit[0] = '\0';

    char buffer[20];

    for (int i = 1; i < 100000; i++) {
        for (int j = 1; j < 10;j++) {
            int product = j * i;
            // printf("%d %d %d \n", i, j, product);

            sprintf(buffer, "%d", product);
            strcat(pandigit, buffer);

            // printf("%s %s \n", pandigit, buffer);
            // printf("Pandigit length: %ld \n", strlen(pandigit));

            if (strlen(pandigit) == 9 && isPandigit(pandigit)){
                printf("The number: %d \n", i);
                printf("The pandigit %s \n", pandigit);
                break;
            }

            if(strlen(pandigit) >= 9) {
                break;
            }
        }

        pandigit[0] = '\0';
        buffer[0] = '\0';

        if(i > 5) break;
    }

    return 1;
}

int isPandigit(char* number) {
    int sum = 0;
    for (int i = 0; i < 9; i++) {
        sum += atoi(&number[i]);
    }

    if (sum == 50) return 1;
    return 0;
}
