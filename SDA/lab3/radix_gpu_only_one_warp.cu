#include <stdlib.h>
#include <cuda_runtime.h>
#include <stdio.h>
#include <thrust/scan.h>

#define N 33
#define BLOCK_SIZE 64

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

void init_array(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }
}

__global__ void count_kernel(int* arr, int* histogram, int n, int divisor) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < n) {
        int abs_num = abs(arr[i]);
        int nth_digit = (abs_num / divisor) % 10;

        atomicAdd(&histogram[nth_digit], 1);
    }
}

__global__ void count_sort_kernel(int* arr, int* offsets, int n, int divisor, int* temp) {
    int i = (n - 1) - (blockIdx.x * blockDim.x + threadIdx.x);

    if (i >= 0) {
        int abs_num = abs(arr[i]);
        int nth_digit = (abs_num / divisor) % 10;

        int pos = atomicSub(&offsets[nth_digit], 1) - 1;

        temp[pos] = arr[i];
    }
}

__global__ void max_num_kernel(int* arr, int n, int* max) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        atomicMax(max, arr[i]);
    }
}

void check_order(int* arr, int n) {
    for (int i = 0; i < (n - 1); i++) {
        if(arr[i] > arr[i+1]) {
            printf("Failed at: %d > %d", arr[i], arr[i+1]);
            printf("\n\nTEST FAILED\n\n");
            return;
        }
    }

    printf("\n\nTEST PASSED\n\n");
}

int main() {
    int* h_arr = (int*)malloc(N * sizeof(int));
    int* h_temp = (int*)malloc(N * sizeof(int));
    int* h_histogram = (int*)malloc(10 * sizeof(int));
    int* h_max_num = (int*)calloc(1, sizeof(int));

    init_array(h_arr, N);

    int* d_arr;
    int* d_histogram;
    int* d_temp;
    int* d_max_num;

    cudaMalloc(&d_arr, N * sizeof(int));
    cudaMalloc(&d_temp, N * sizeof(int));
    cudaMalloc(&d_histogram, 10 * sizeof(int));
    cudaMalloc(&d_max_num, 1 * sizeof(int));

    cudaMemcpy(d_arr, h_arr, N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_histogram, h_histogram, 10 * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_max_num, h_max_num, 1 * sizeof(int), cudaMemcpyHostToDevice);

    dim3 blockDim(BLOCK_SIZE);
    dim3 gridDim((N + BLOCK_SIZE - 1) / BLOCK_SIZE);

    max_num_kernel<<<gridDim, blockDim>>>(d_arr, N, d_max_num);
    cudaMemcpy(h_max_num, d_max_num, 1 * sizeof(int), cudaMemcpyDeviceToHost);
    cudaFree(d_max_num);

    int max_digits = 1;

    while (*h_max_num >= 10) {
        *h_max_num /= 10;
        max_digits++;
    }

    for (int digit = 0; digit < max_digits; digit++) {
        int divisor = pow(10, digit);

        cudaMemset(d_histogram, 0, 10 * sizeof(int));
        count_kernel<<<gridDim, blockDim>>>(d_arr, d_histogram, N, divisor);
        cudaDeviceSynchronize();

        cudaMemcpy(h_histogram, d_histogram, 10 * sizeof(int), cudaMemcpyDeviceToHost);
        for (int i = 1; i < 10; i++) {
            h_histogram[i] += h_histogram[i - 1];
        }

        cudaMemcpy(d_histogram, h_histogram, 10 * sizeof(int), cudaMemcpyHostToDevice);
        cudaDeviceSynchronize();

        count_sort_kernel<<<gridDim, blockDim>>>(d_arr, d_histogram, N, divisor, d_temp);
        cudaDeviceSynchronize();

        cudaMemcpy(d_arr, d_temp, N * sizeof(int), cudaMemcpyDeviceToDevice);
    }

    cudaMemcpy(h_arr, d_arr, N * sizeof(int), cudaMemcpyDeviceToHost);
    check_order(h_arr, N);

    printf("Sorted array: \n");
    for (int i = 0; i < N; i++) {
        printf("%d ", h_arr[i]);
    }
    printf("\n");

    free(h_max_num);
    free(h_histogram);
    free(h_arr);
    free(h_temp);

    cudaFree(d_max_num);
    cudaFree(d_histogram);
    cudaFree(d_arr);
    cudaFree(d_temp);

    return 0;
}
