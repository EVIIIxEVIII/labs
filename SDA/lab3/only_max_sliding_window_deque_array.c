#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double getTimeMicroseconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;
}

void pop_left(int* arr, size_t* size) {
    if (*size == 0) return;
    for (size_t i = 0; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
}

void pop(int* arr, size_t* size) {
    if (*size == 0) return;
    (*size)--;
}

void push(int* arr, size_t* size, int element) {
    arr[*size] = element;
    (*size)++;
}

int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    if (numsSize == 0 || k == 0) {
        *returnSize = 0;
        return NULL;
    }

    *returnSize = numsSize - k + 1;
    int* res = (int*)malloc((*returnSize) * sizeof(int));
    if (!res) return NULL;

    int* deque = (int*)malloc(numsSize * sizeof(int));
    if (!deque) {
        free(res);
        return NULL;
    }
    size_t dequeLen = 0;

    for (int i = 0; i < k; i++) {
        while (dequeLen > 0 && nums[deque[dequeLen - 1]] < nums[i]) {
            pop(deque, &dequeLen);
        }
        push(deque, &dequeLen, i);
    }
    res[0] = nums[deque[0]];

    for (int i = k; i < numsSize; i++) {
        if (dequeLen > 0 && deque[0] == i - k) {
            pop_left(deque, &dequeLen);
        }

        while (dequeLen > 0 && nums[deque[dequeLen - 1]] < nums[i]) {
            pop(deque, &dequeLen);
        }
        push(deque, &dequeLen, i);
        res[i - k + 1] = nums[deque[0]];
    }

    free(deque);
    return res;
}

int main() {
    int n;
    printf("Input the number of elements: ");
    scanf("%d", &n);

    int* nums = (int*)malloc(n * sizeof(int));
    if (!nums) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Input the array elements: \n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    int k;
    printf("Input k: ");
    scanf("%d", &k);

    if (k > n) {
        printf("k cannot be bigger than n\n");
        free(nums);
        return 1;
    }

    int returnSize;

    double start = getTimeMicroseconds();
    int* result = maxSlidingWindow(nums, n, k, &returnSize);
    double end = getTimeMicroseconds();

    printf("\n%lf\n", (end - start));

    printf("Sliding window maximums: ");
    for (int i = 0; i < returnSize; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    free(nums);
    free(result);
    return 0;
}

