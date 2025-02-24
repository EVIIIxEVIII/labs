#include <stdio.h>
#include <malloc.h>

void pop_left(int* arr, size_t* size) {
    if (*size == 0) return;
    for (size_t i = 0; i < *size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    (*size)--;
}

void pop(int* arr, size_t* size) {
    arr[*size - 1] = 0;
    (*size)--;
}

void push(int* arr, size_t* size, int element) {
    arr[*size] = element;
    (*size)++;
}

int* max_sliding_window(int k, int n, int* arr, size_t* resLen) {
    int* res = (int*)malloc(k * sizeof(int));

    int* deque = (int*)malloc(k * sizeof(int));
    size_t dequeLen = 0;

    for (int i = 0; i < k; i++) {
        while (dequeLen > 0 && deque[dequeLen - 1] < arr[i]) {
            pop(deque, &dequeLen);
        }
        push(deque, &dequeLen, i);
    }
    push(res, resLen, arr[deque[0]]);

    int l = 1;
    int r = k;

    while (r <= n - 1) {
        if (dequeLen > 0 && deque[0] == l - 1) {
            pop_left(deque, &dequeLen);
        }

        while (dequeLen > 0 && arr[deque[dequeLen - 1]] < arr[r]) {
            pop(deque, &dequeLen);
        }

        push(deque, &dequeLen, r);
        push(res, resLen, arr[deque[0]]);

        l++; r++;
    }

    free(deque);
    return res;
}

int main() {
    int n;
    printf("Input the number of elements: ");
    scanf("%d", &n);
    printf("\n");

    int* arr = (int*)malloc(n * sizeof(int));
    if(!arr) {
        printf("\nFailed to allocate memory!\n");
        return 0;
    }

    printf("Input the array elements: \n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int k;
    printf("\n");
    printf("Input k: ");
    scanf("%d", &k);
    printf("\n");

    if (k > n) {
        printf("k cannot be bigger than n");
        return 0;
    }

    size_t resLen = 0;
    int* res = max_sliding_window(k, n, arr, &resLen);

    printf("\nThe result: ");
    for (int i = 0; i < resLen; i++) {
        printf("%d ", res[i]);
    }

    free(arr);
    free(res);
    return 0;
}


