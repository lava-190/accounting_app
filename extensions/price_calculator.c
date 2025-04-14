// extensions/price_calculator.c
#include <stddef.h>

// Function to calculate the total of an array of doubles
double calculate_total(const double *prices, size_t length) {
    double total = 0;
    for (size_t i = 0; i < length; i++) {
        total += prices[i];
    }
    return total;
}
