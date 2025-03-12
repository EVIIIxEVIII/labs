#include <stdio.h>
#include <stdbool.h>
#include <malloc.h>
#include <stdlib.h>
#include <string.h>

// price,area,bedrooms,bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus

const int FIELDS = 13;

enum FurnishStatus {
    FURNISHED,
    SEMI_FURNISHED,
    UNFURNISHED,
};

struct House {
    float price;
    float area;
    int bedrooms;
    int bathrooms;
    int stories;
    bool mainroad;
    bool guestroom;
    bool basement;
    bool hotwaterheating;
    bool airconditioning;
    int parking;
    bool prefarea;
    enum FurnishStatus furnishingstatus;
};

struct House* readCSVFile(const char* src) {
    FILE *file = fopen(src, "r");
	if (file == NULL) {
		perror("Error opening file");
		return NULL;
	}

    int linesNum = -1;
    char _[1024];
	while (fgets(_, sizeof(_), file)) linesNum++;

    printf("\nNumber of lines: %d\n", linesNum);
    rewind(file);

    struct House* data = malloc(linesNum * sizeof(struct House));

    char buffer[2048];
    int i = 0;
	while (fgets(buffer, sizeof(buffer), file)) {
        i++; if (i == 1) continue;

        struct House house;
        memset(&house, 0, sizeof(struct House));

        char* token = strtok(buffer, ",");
        if (token == NULL) continue;
        house.price = strtof(token, NULL);

        token = strtok(NULL, ",");
        if (token == NULL) continue;
        house.area = strtof(token, NULL);

        token = strtok(NULL, ",");
        if (token == NULL) continue;
        house.bedrooms = strtof(token, NULL);

        token = strtok(NULL, ",");
        if (token == NULL) continue;
        house.bathrooms = strtof(token, NULL);

        token = strtok(NULL, ",");
        if (token == NULL) continue;
        house.stories = strtof(token, NULL);

        token = strtok(NULL, ",");
        if (token == NULL) continue;
        house.mainroad = (bool)strtof(token, NULL);

        break;
    }

    fclose(file);
}

int main() {
    readCSVFile("./data/Housing.csv");


}

