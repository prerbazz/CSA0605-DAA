#include <stdio.h>

#define MAX_SIZE 100

void rearrangeArray(int arr[], int size) {
    int evenIndex = 0;
    int oddIndex = 1;

    // Create a temporary array to hold the rearranged elements
    int temp[MAX_SIZE];

    // Initialize the temporary array with -1 (or any invalid value)
    for (int i = 0; i < size; i++) {
        temp[i] = -1;
    }

    // Place even elements at even indices
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            if (evenIndex < size) {
                temp[evenIndex] = arr[i];
                evenIndex += 2;
            }
        }
    }

    // Place odd elements at odd indices
    for (int i = 0; i < size; i++) {
        if (arr[i] % 2 != 0) {
            if (oddIndex < size) {
                temp[oddIndex] = arr[i];
                oddIndex += 2;
            }
        }
    }

    // Copy the rearranged elements back to the original array
    for (int i = 0; i < size; i++) {
        arr[i] = temp[i];
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[MAX_SIZE];
    int size;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &size);

    if (size > MAX_SIZE) {
        printf("Size exceeds the maximum allowed size of %d\n", MAX_SIZE);
        return 1;
    }

    printf("Enter %d elements:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }

    rearrangeArray(arr, size);

    printf("Rearranged array:\n");
    printArray(arr, size);

    return 0;
}
