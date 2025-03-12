#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct Node {
    int val;
    struct Node* next;
    struct Node* prev;
} Node;

typedef struct {
    Node* start;
    Node* end;
} Dequeue;

double getTimeMicroseconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;
}

void pop_left(Dequeue* deq, size_t* size) {
    if (*size == 0 || !deq->start) return;

    Node* temp = deq->start;
    deq->start = deq->start->next;

    if (deq->start) {
        deq->start->prev = NULL;
    } else {
        deq->end = NULL;
    }

    free(temp);
    (*size)--;
}

void pop(Dequeue* deq, size_t* size) {
    if (*size == 0 || !deq->end) return;

    Node* temp = deq->end;
    deq->end = deq->end->prev;

    if (deq->end) {
        deq->end->next = NULL;
    } else {
        deq->start = NULL;
    }

    free(temp);
    (*size)--;
}

void push(Dequeue* deq, size_t* size, int element) {
    Node* node = (Node*)malloc(sizeof(Node));
    if (!node) {
        perror("Failed to allocate memory");
        return;
    }

    node->val = element;
    node->next = NULL;
    node->prev = deq->end;

    if (deq->end) {
        deq->end->next = node;
    } else {
        deq->start = node;
    }

    deq->end = node;
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

    Dequeue deque = { NULL, NULL };
    size_t dequeLen = 0;

    for (int i = 0; i < k; i++) {
        while (dequeLen > 0 && nums[deque.end->val] < nums[i]) {
            pop(&deque, &dequeLen);
        }
        push(&deque, &dequeLen, i);
    }
    res[0] = nums[deque.start->val];

    for (int i = k; i < numsSize; i++) {
        if (dequeLen > 0 && deque.start->val == i - k) {
            pop_left(&deque, &dequeLen);
        }

        while (dequeLen > 0 && nums[deque.end->val] < nums[i]) {
            pop(&deque, &dequeLen);
        }
        push(&deque, &dequeLen, i);
        res[i - k + 1] = nums[deque.start->val];
    }

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

