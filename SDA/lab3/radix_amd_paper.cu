#include <cuda_runtime.h>
#include <stdio.h>

#define BLOCK_SIZE 32
#define N 4

void __global__ compute_offset_table(int* arr, int n, int* global, int chunk) {
    __shared__ int local_offset_map[4];
    __shared__ int sum;

    int gId = blockIdx.x * blockDim.x + threadIdx.x;
    int tid = threadIdx.x;

    if (tid == 0) sum = 0;
    if (tid < 4) local_offset_map[tid] = 0;
    __syncthreads();

    if (gId < n) {
        int digit = (arr[gId] >> (2 * chunk)) & 3;
        atomicAdd(&local_offset_map[digit], 1);
    }
    __syncthreads();

    if (tid < 4) {
        atomicAdd(&global[tid], local_offset_map[tid]);
    }
    __syncthreads();

    if (tid < 4) {
        atomicAdd(&sum, local_offset_map[tid]);
    }
    __syncthreads();
}

void init_array(int* arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }
}

int main() {
    int* h_arr = (int*)malloc(N * sizeof(int));
    int* h_res = (int*)malloc(4 * sizeof(int));

    init_array(h_arr, N);

    printf("Initial array: \n");
    for (int i = 0; i < N; i++) {
       printf("%b ", h_arr[i]);
    }
    printf("\n");

    printf("First chunk digits: \n");
    for (int i = 0; i < N; i++) {
        printf("%d ", (h_arr[i] >> (2 * 0)) & 3);
    }
    printf("\n");

    int* d_arr;
    int* d_res;

    cudaMalloc(&d_arr, N * sizeof(int));
    cudaMalloc(&d_res, N * sizeof(int));

    cudaMemcpy(d_arr, h_arr, N * sizeof(int), cudaMemcpyHostToDevice);

    dim3 blockDim(BLOCK_SIZE);
    dim3 gridDim((N + BLOCK_SIZE - 1) / BLOCK_SIZE);

    compute_offset_table<<<gridDim, blockDim>>>(d_arr, N, d_res, 0);

    cudaMemcpy(h_res, d_res, N * sizeof(int), cudaMemcpyDeviceToHost);

    printf("Offset map: \n");
    for (int i = 0; i < 4; i++) {
       printf("%d ", h_res[i]);
    }
    printf("\n");


}
