#include <stdio.h>
#include <stdlib.h>

/*
    We'll be using switch case to convert numbers to their roman numeral
    Here we'll be purely using switch with no looping involved
    The maximum roman numeral is MMMCMXCIX (3999), so we'll include a simple error handler with if
*/

int main() {

    int num;
    printf("Enter number: "); // sample input: 2267
    scanf("%d",&num); // scans input
    
    if (num > 4000) {
        printf("The maximum input is 3999\nExiting Program..");
        exit(0); 
    } // exits program if input is 4000 or more

    printf("Roman equivalent is: "); // prints out MMDCLXVII

    switch(num / 1000) { // 2667 / 1000 = 2.667
        case 3:
            printf("MMM");
            break;
        case 2:
            printf("MM"); // gets this
            break;
        case 1:
            printf("M");
    }

    switch((num % 1000) / 100) { // 667 / 1000 = 0.667, 667 / 100 = 6.67
        case 9:
            printf("CM");
            break;
        case 8:
            printf("DCCC");
            break;
        case 7:
            printf("DCC");
            break;
        case 6:
            printf("DC"); // gets this
            break;
        case 5:
            printf("D");
            break;
        case 4:
            printf("CD");
            break;
        case 3:
            printf("CCC");
            break;
        case 2:
            printf("CC");
            break;
        case 1:
            printf("C");
    }

    switch((num % 100) / 10) { // 67 / 100 = 0.67, 67 / 10 = 6.7
        case 9:
        printf("XC");
            break;
        case 8:
            printf("LXXX");
            break;
        case 7:
            printf("LXX");
            break;
        case 6:
            printf("LX"); // gets this
            break;
        case 5:
            printf("L");
            break;
        case 4:
            printf("XL");
            break;
        case 3:
            printf("XXX");
            break;
        case 2:
            printf("XX");
            break;
        case 1:
            printf("X");
    }

    switch(num % 10) { // 7 / 10 = 0.7, 7
        case 9:
            printf("IX");
            break;
        case 8:
            printf("VIII");
            break;
        case 7:
            printf("VII"); // gets this
            break;
        case 6:
            printf("VI");
            break;
        case 5:
            printf("V");
            break;
        case 4:
            printf("IV");
            break;
        case 3:
            printf("III");
            break;
        case 2:
            printf("II");
            break;
        case 1:
            printf("I");
            break;
        default:
            printf("Input positive numbers.");
    }

        // output: 2667 = MMDCLXVII

    return 0;
}