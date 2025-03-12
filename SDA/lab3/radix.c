#include <math.h>
#include <stdlib.h>
#include <stdio.h>

int get_nth_digit(int num, int digit) {
    int abs_num = abs(num);
    int divisor = 1;

    for (int i = 0; i < digit; i++) {
        divisor *= 10;
    }

    return (abs_num / divisor) % 10;
}

void count_sort(int* array, int digit, size_t n) {
    int count[10] = {0};
    int* tempMap = (int*)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int nth_digit = get_nth_digit(array[i], digit);
        count[nth_digit]++;
    }

    // compute the offsets inside the count arr
    for (int i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    for (int i = n-1; i >= 0; i--) {
        int nth_digit = get_nth_digit(array[i], digit);

        tempMap[count[nth_digit] - 1] = array[i];
        count[nth_digit] -= 1;
    }

    for (int i = 0; i < n; i++) {
        array[i] = tempMap[i];
    }

    free(tempMap);
}

void radix(int* array, size_t n) {
    int maxNumber = 0;
    for (int i = 0; i < n; i++) maxNumber = fmax(maxNumber, array[i]);
    int maxDigits = ceil(log10(maxNumber));

    for (int i = 0; i < maxDigits; i++) {
        count_sort(array, i, n);
    }
}

int main() {
    int arr[8] = {170, 45, 75, 90, 802, 24, 2, 66};

    radix(arr, 8);

    for (int i = 0; i < 8; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}
