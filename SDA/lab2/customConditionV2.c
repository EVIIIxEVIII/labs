// Based on the research I did Insert Sort is faster for smaller arrays
// (<= 32 elements), while Merge Sort is much better for large arrays (32 > elements)
//
// Condition:
// Given a 1D array with integers, read from keyboard or from a binary file (use command line args to specify the file).
// Write the following C functions (with subsequent calls to the main) that are able:
// 1) Sort the array in ascending order using insertion sort for arrays with <= 32 elements
// 2) Sort the array in ascending order using Merge Sort for arrays with >= 32 elements

#include <stddef.h>
#include <stdio.h>
#include <time.h>
#include <malloc.h>
#include <stdlib.h>

void readFromKeyboard(size_t* numberOfElements, int** data);
void readFromFile(size_t* numberOfElements, int** data, char* fileName);
void insertSort(size_t numberOfElements, int* data);
void mergeSort(size_t n, int* data);
void merge(int* data, int left, int mid, int right, int* temp);

double getTimeMicroseconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;
}

int main(int argc, char *argv[]) {
    size_t numberOfElements = 0;
    int* data = NULL;

    if (argc == 1) {
        readFromKeyboard(&numberOfElements, &data);
    } else {
        readFromFile(&numberOfElements, &data, argv[1]);
    }

    double start = getTimeMicroseconds();

    if (numberOfElements <= 32) {
        insertSort(numberOfElements, data);
    } else {
        mergeSort(numberOfElements, data);
    }

    double end = getTimeMicroseconds();

    numberOfElements <= 32 ?
        printf("Used insertion sort to sort all the elements!") :
        printf("Used merge sort to sort all the elements!");

    printf("\nINDEX | VALUE\n");
    for (int i = 0; i < numberOfElements; i++) {
        printf("  %d      %d\n", i, data[i]);
    }

	printf("\n\nExecution in microseconds: %f\n\n", end - start);

    free(data);
    return 0;
}

void insertSort(size_t numberOfElements, int* data) {
    // check for edge case
    if (numberOfElements <= 1) return;

    for (size_t i = 1; i < numberOfElements; i++) {
        int val = data[i];
        // j is the element which comes before the current one
        int j = i - 1;

        // while j is greater than 0 and the value at j is greater than our value
        while (j >= 0 && data[j] > val) {
            // we move each element to the right of the array.
            data[j + 1] = data[j];
            // and then decrease our j
            j--;
        }

        // after we found the correct place for our value
        // we insert it there.
        data[j + 1] = val;
    }
}

void mergeSort(size_t n, int* data) {
    int* temp = malloc(n * sizeof(int));
    if (!temp) {
        perror("Failed to allocate memory!");
        exit(1);
    }

    // width of the subarrays
    for (int width = 1; width < n; width *= 2) {
        // here we have 2 * width, because we are mergin 2 subarrays

        #pragma omp parallel for
        for (int i = 0; i < n; i += 2 * width) {

            int left = i;
            // these conditions are needed so that mid and right don't exceed the
            // array length
            int mid = (i + width < n) ? i + width : n;
            int right = (i + 2 * width < n) ? i + 2 * width : n;

            __builtin_prefetch(&data[right], 1, 3);

            merge(data, left, mid, right, temp);
        }
    }

    free(temp);
}

void merge(int* data, int left, int mid, int right, int* temp) {
// i is for the left array, j is for the right array and k is for the temp array
    int i = left, j = mid, k = left;
// while the index for the left array is inside its bounds
// adn the index of the right array is inside its bounds
	while (i < mid && j < right) {
// we want to compare the corresponding elements from each array
// if the value of the right array is bigger we want to copy
// the value of the left array to our temp
		if (data[i] <= data[j]) {
			temp[k] = data[i];
            k++; i++;
        }
// otherwise if the left array has a bigger value, we copy the
// value of the right array into our temp
		else {
			temp[k] = data[j];
            k++; j++;
        }
	}

    // copy the remaining elements from left
    while(i < mid) {
        temp[k] = data[i];
        k++; i++;
    }

    // copy the remaining elements from right
    while(j < right) {
        temp[k] = data[j];
        k++; j++;
    }

    for (i = left; i < right; i++) {
        data[i] = temp[i];
    }
}

void readFromKeyboard(size_t* numberOfElements, int** data) {
    printf("Input the number of elements: ");
    scanf("%ld", numberOfElements);
    *data = malloc(*numberOfElements * sizeof(int));

    printf("\nInput the elements separated by space: \n");
    if (*data == NULL) exit(1);
    for (int i = 0; i < *numberOfElements; i++) {
        scanf("%d", &(*data)[i]);
    }
}

void readFromFile(size_t* numberOfElements, int** data, char* fileName) {
    FILE *file = fopen(fileName, "rb");

    if (!file) {
        perror("Error opening file");
        exit(1);
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    if (file_size < 0) {
		perror("Error getting file size");
		fclose(file);
		exit(1);
	}
    rewind(file);

    *numberOfElements = file_size / sizeof(int);
    *data = (int*)malloc(*numberOfElements * sizeof(int));
    if (!data) {
        perror("Memory allocation failed");
        fclose(file);
        exit(1);
    }

    size_t elements_read = fread(*data, sizeof(int), *numberOfElements, file);
	if (elements_read != *numberOfElements) {
		perror("Error reading file");
		free(data);
		fclose(file);
		exit(1);
	}

    fclose(file);
}

