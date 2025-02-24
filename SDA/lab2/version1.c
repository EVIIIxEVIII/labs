#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <malloc.h>

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
    scanf("%d", &n);

    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
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
	printf("\n\nElapsed time: %f\n\n", end - start);

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
    int swapped;
    for (int i = 0; i < size; i++) {
        // define a flag variable to optimize
        swapped = 0;

        for (int j = 0; j < size - 1; j++) {
            if (arr[j] < arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] =  temp;
                swapped = 1;
            }
        }

        // if the swap did not occur it means that the array
        // is already sorted and no more operations are needed.
        if (!swapped) break;
    }
}

void selectionSort(int* arr, int size) {
    for (int i = 0; i < size; i++) {
        int min = i;

        // for each element go through all the elements after it
        // and then find the smallest. When the smallest is found
        // swap it with the current element
        for (int j = i; j < size; j++) {
            if(arr[min] > arr[j]) {
                min = j;
            }
        }

        if (min != i) {
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
}

