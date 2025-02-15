#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <ctime>

double getTimeMicroseconds() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1e6 + ts.tv_nsec / 1e3;
}

std::vector<int> loadBinaryFile(const std::string& filename) {
    std::ifstream file(filename, std::ios::binary);
    if (!file) {
        std::cerr << "Error opening file: " << filename << std::endl;
        exit(1);
    }

    file.seekg(0, std::ios::end);
    size_t fileSize = file.tellg();
    file.seekg(0, std::ios::beg);

    size_t numElements = fileSize / sizeof(int);
    std::vector<int> data(numElements);

    file.read(reinterpret_cast<char*>(data.data()), fileSize);

    if (!file) {
        std::cerr << "Error reading file: " << filename << std::endl;
        exit(1);
    }

    file.close();
    return data;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <binary_file>" << std::endl;
        return 1;
    }

    std::string filename = argv[1];

    std::vector<int> data = loadBinaryFile(filename);
    size_t numElements = data.size();

    std::cout << "Loaded " << numElements << " elements from " << filename << std::endl;

    double start = getTimeMicroseconds();
    std::sort(data.begin(), data.end());
    double end = getTimeMicroseconds();

    std::cout << "Sorting time: " << (end - start) << " microseconds" << std::endl;

    return 0;
}

