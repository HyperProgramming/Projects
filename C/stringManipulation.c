#include <stdio.h>
#include <string.h>

/*
    Basic string manipulation in C
    Take two strings then print them in a specific order
    We'll use fgets and strcspn (string complementary span) to properly store and manipulate data
    fgets stores and reads only the set size from input
    strcspn manipulates the stored data to remove the unnecessary newline
*/

int main() {
    char first[100], second[100];

    printf("Enter the first string: "); // sample input: "hello world"
    fgets(first, sizeof(first), stdin); // read user input safely
    first[strcspn(first, "\n")] = 0; // removes unwanted newline characters

    printf("Enter the second string: "); // sample input: "world hello"
    fgets(second, sizeof(second), stdin); // read user input safely
    second[strcspn(second, "\n")] = 0; // removes unwanted newline characters

    printf("%s %s %s", first, second, first); // sample output: "hello world hello" / "hello world world hello hello world"

    return 0;
}