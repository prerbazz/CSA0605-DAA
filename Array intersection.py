#include <stdio.h>
#include <stdlib.h>

// Function to compare two integers (used in qsort)
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

// Function to find the intersection of two arrays
void findIntersection(int *nums1, int size1, int *nums2, int size2) {
    // Sort both arrays
    qsort(nums1, size1, sizeof(int), compare);
    qsort(nums2, size2, sizeof(int), compare);

    int i = 0, j = 0;
    
    printf("Intersection of the two arrays: ");
    // Use two pointers to find the intersection
    while (i < size1 && j < size2) {
        // Skip duplicates in nums1
        if (i > 0 && nums1[i] == nums1[i - 1]) {
            i++;
            continue;
        }
        
        // Skip duplicates in nums2
        if (j > 0 && nums2[j] == nums2[j - 1]) {
            j++;
            continue;
        }

        if (nums1[i] < nums2[j]) {
            i++;
        } else if (nums1[i] > nums2[j]) {
            j++;
        } else {
            // Common element found
            printf("%d ", nums1[i]);
            i++;
            j++;
        }
    }
    printf("\n");
}

int main() {
    int nums1[] = {4, 9, 5, 9};
    int nums2[] = {9, 4, 9, 8, 4};

    int size1 = sizeof(nums1) / sizeof(nums1[0]);
    int size2 = sizeof(nums2) / sizeof(nums2[0]);

    // Find and print the intersection of nums1 and nums2
    findIntersection(nums1, size1, nums2, size2);

    return 0;
}
