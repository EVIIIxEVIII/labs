#include <stdio.h>

// struct that holds a date
typedef struct {
    int day;
    int month;
    int year;
} Date;

// chek if a yer is leap, meaning feb gets 29 days instead of 28
int is_leap_year(int year) {
    return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

// return how many days are in a month, since not all months are the same
int days_in_month(int month, int year) {
    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            return 31; // 31 day months
        case 4: case 6: case 9: case 11:
            return 30; // 30 day months
        case 2:
            return is_leap_year(year) ? 29 : 28; // feb is tricky bc of leap years
        default:
            return -1; // wrong month :((
    }
}

// get the next day, so like move forward by 1 day
Date next_date(Date current) {
    Date next = current;
    int days = days_in_month(current.month, current.year);

    if (current.day < days) {
        next.day++; // just move to next day
    } else {
        next.day = 1; // reset day to 1 since we go to next month
        if (current.month == 12) { // if it's december, we jump to next year
            next.month = 1;
            next.year++;
        } else {
            next.month++; // else just move to next month
        }
    }

    return next;
}

int main() {
    Date input_date;

    // ask user for a date
    printf("enter date (DD MM YYYY): ");
    if (scanf("%d %d %d", &input_date.day, &input_date.month, &input_date.year) != 3) {
        printf("bro that's not a valid format\n");
        return 1;
    }

    // make sure date is legit
    if (input_date.month < 1 || input_date.month > 12 || input_date.day < 1 || input_date.day > days_in_month(input_date.month, input_date.year)) {
        printf("nah that date ain't real\n");
        return 1;
    }

    // get the next day
    Date next = next_date(input_date);

    // print the result
    printf("next date: %02d/%02d/%04d\n", next.day, next.month, next.year);

    return 0;
}

