#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <malloc.h>
#include <immintrin.h>

int printNonDuplicates(int* arr, int size);
void bubbleSort(int* arr, int size);
void selectionSort(int* arr, int size);

double getTimeMicroseconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;
}

int main() {
    int n = 0;

    printf("Input the number of elements: ");
    int _ = scanf("%d", &n);

    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int _ = scanf("%d", &arr[i]);
    }

    double start = getTimeMicroseconds();

    printf("\n1) Find and display all non-duplicate array elements.\n");
    int containsDup = printNonDuplicates(arr, n);

    if (containsDup) { // bubble sort is stable that's why we do it if there are duplicates
        printf("\n2) If the array contains duplicates perform a descending bubble sort. \n");
        bubbleSort(arr, n);
        printf("\nElements after descending bubble sort: \n");
        for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    } else { // selection sort is not stable that's why we do it iff there are no duplicates
        printf("\n2) If the array does not contains duplicates perform an ascending selection sort. \n");
        selectionSort(arr, n);
        printf("\nElements after ascending selection sort: \n");
        for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    }

    double end = getTimeMicroseconds();
	printf("\n\nExecution in microseconds: %f\n\n", end - start);

    return 0;
}

int printNonDuplicates(int* arr, int size) {
    int sum = 0;
    int containsDup = 0;
    int tableHeadPrinted = 0;

    for (int i = 0; i < size; i++) {
        int count = 0;

        for (int j = 0; j < size; j++) {
            if (arr[i] == arr[j]) {
                count++;
            }
        }

        if (count == 1 && !tableHeadPrinted) {
            printf("\n\n INDEX   |  VALUE \n");
            tableHeadPrinted = 1;
        }

        if (count == 1) {
            printf("   %d          %d\n", i, arr[i]);
            sum += arr[i];
            continue;
        }

        containsDup = 1;
    }

    if (sum > 0) printf("The sum is: %d \n\n", sum);
    else printf("There are only duplicates in the array!\n\n");

    return containsDup;
}

void bubbleSort(int* arr, int size) {
    int swapped = 0;
    for (int i = 0; i < size; i++) {
        swapped = 0;

        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] < arr[j+1]) {
                arr[j] ^= arr[j + 1];
                arr[j + 1] ^= arr[j];
                arr[j] ^= arr[j + 1];
// the property that x ^ y ^ x = y and y ^ x ^ y = x is used here.
// let us denote arr[j] as x and arr[j + 1] as y
// basically in the first line we get (x ^ y)
// then in the second line we do y ^ x ^ y = x
// finally in the third line we do x ^ y ^ x = y
// thus we swapped the values

                swapped = 1;
            }
        }

        if (!swapped) break;
    }
}

void selectionSort(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        int minIndex = i;
        __m256i minVal = _mm256_set1_epi32(arr[i]); // Initialize SIMD min with arr[i]

        for (int j = i + 1; j < size; j += 8) {
            __m256i curr = _mm256_loadu_si256((__m256i*)&arr[j]); // Load 8 elements
            __m256i mask = _mm256_cmpgt_epi32(minVal, curr); // Compare with current min
            minVal = _mm256_blendv_epi8(minVal, curr, mask); // Update min if needed

            // Scalar fallback to store the actual min index (SIMD doesn't track indices)
            for (int k = 0; k < 8 && (j + k) < size; k++) {
                if (arr[j + k] < arr[minIndex]) {
                    minIndex = j + k;
                }
            }
        }

        if (minIndex != i) {
            arr[i] ^= arr[minIndex];
            arr[minIndex] ^= arr[i];
            arr[i] ^= arr[minIndex];
        }
    }
}
